from flask import Flask, render_template, request
import os

from nlp.process_resume import process_resume
from nlp.jd_analyzer import (
    analyze_job_description,
    compare_resume_with_jd
)
from nlp.similarity import calculate_similarity
from nlp.ats_analyzer import analyze_ats
from nlp.resume_improver import generate_improvement_suggestions
from nlp.keyword_analyzer import analyze_keywords
from nlp.resume_info_extractor import extract_resume_information


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        # ==========================================
        # GET INPUT
        # ==========================================

        resume_file = request.files.get("resume")

        job_description = request.form.get(
            "job_description"
        )

        if not resume_file:

            return render_template(
                "index.html",
                error="Please upload a resume."
            )

        if not job_description:

            return render_template(
                "index.html",
                error="Please enter a job description."
            )


        # ==========================================
        # SAVE RESUME
        # ==========================================

        os.makedirs(
            UPLOAD_FOLDER,
            exist_ok=True
        )

        resume_path = os.path.join(
            UPLOAD_FOLDER,
            resume_file.filename
        )

        resume_file.save(resume_path)


        try:

            # ==========================================
            # 1. PROCESS RESUME
            # ==========================================

            resume_result = process_resume(
                resume_path
            )

            resume_text = resume_result["text"]

            resume_skills = resume_result["skills"]


            # ==========================================
            # 2. RESUME INFORMATION
            # ==========================================

            resume_info = extract_resume_information(
                resume_text
            )


            # ==========================================
            # 3. JOB DESCRIPTION
            # ==========================================

            jd_result = analyze_job_description(
                job_description
            )

            required_skills = (
                jd_result["required_skills"]
            )


            # ==========================================
            # 4. SMART SKILL MATCHING
            # ==========================================

            comparison = compare_resume_with_jd(
                resume_skills,
                required_skills
            )

            skill_match = (
                comparison["match_percentage"]
            )


            # ==========================================
            # 5. NLP SIMILARITY
            # ==========================================

            similarity_score = calculate_similarity(
                resume_text,
                job_description
            )


            # ==========================================
            # 6. ATS ANALYSIS
            # ==========================================

            ats_result = analyze_ats(
                resume_text
            )

            ats_score = (
                ats_result["section_score"]
            )


            # ==========================================
            # 7. KEYWORD ANALYSIS
            # ==========================================

            keyword_result = analyze_keywords(
                resume_text,
                job_description
            )

            keyword_score = (
                keyword_result["keyword_score"]
            )


            # ==========================================
            # 8. OVERALL SCORE
            # ==========================================

            overall_score = (

                (skill_match * 0.35)

                +

                (similarity_score * 0.25)

                +

                (ats_score * 0.20)

                +

                (keyword_score * 0.20)

            )

            overall_score = round(
                overall_score,
                2
            )


            # ==========================================
            # 9. RECOMMENDATION
            # ==========================================

            if overall_score >= 80:

                recommendation = (
                    "Excellent match! "
                    "Your resume is highly suitable "
                    "for this job."
                )

            elif overall_score >= 60:

                recommendation = (
                    "Good match! "
                    "Improve the missing skills and "
                    "important keywords."
                )

            elif overall_score >= 40:

                recommendation = (
                    "Moderate match. "
                    "Your resume needs improvement "
                    "before applying."
                )

            else:

                recommendation = (
                    "Low match. "
                    "Consider improving your skills, "
                    "keywords and resume structure."
                )


            # ==========================================
            # 10. IMPROVEMENT SUGGESTIONS
            # ==========================================

            improvement_suggestions = (
                generate_improvement_suggestions(

                    comparison[
                        "missing_skills"
                    ],

                    ats_result[
                        "suggestions"
                    ],

                    overall_score

                )
            )


            # ==========================================
            # 11. FINAL RESULT
            # ==========================================

            result = {

                # ---------------- SCORES ----------------

                "skill_match":
                    skill_match,

                "similarity":
                    similarity_score,

                "ats_score":
                    ats_score,

                "keyword_score":
                    keyword_score,

                "overall_score":
                    overall_score,


                # ---------------- SKILLS ----------------

                "matching_skills":
                    comparison[
                        "matching_skills"
                    ],

                "missing_skills":
                    comparison[
                        "missing_skills"
                    ],

                "resume_skills":
                    resume_skills,

                "required_skills":
                    required_skills,


                # ---------------- ATS ----------------

                "sections":
                    ats_result[
                        "sections"
                    ],

                "ats_suggestions":
                    ats_result[
                        "suggestions"
                    ],


                # ---------------- KEYWORDS ----------------

                "keywords":
                    keyword_result[
                        "keywords"
                    ],

                "found_keywords":
                    keyword_result[
                        "found_keywords"
                    ],

                "missing_keywords":
                    keyword_result[
                        "missing_keywords"
                    ],


                # ---------------- RESUME INFO ----------------

                "email":
                    resume_info[
                        "email"
                    ],

                "phone":
                    resume_info[
                        "phone"
                    ],

                "linkedin":
                    resume_info[
                        "linkedin"
                    ],

                "github":
                    resume_info[
                        "github"
                    ],

                "education":
                    resume_info[
                        "education"
                    ],

                "experience":
                    resume_info[
                        "experience"
                    ],

                "projects":
                    resume_info[
                        "projects"
                    ],


                # ---------------- IMPROVEMENT ----------------

                "improvement_suggestions":
                    improvement_suggestions,


                # ---------------- RECOMMENDATION ----------------

                "recommendation":
                    recommendation

            }


        except Exception as e:

            return render_template(
                "index.html",
                error=f"Error analyzing resume: {e}"
            )


    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )