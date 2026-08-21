from nlp.process_resume import process_resume
from nlp.jd_analyzer import analyze_job_description, compare_resume_with_jd
from nlp.similarity import calculate_similarity


def main():

    print("=" * 60)
    print("                 AI RESUME ANALYZER")
    print("=" * 60)

    # ==========================================
    # STEP 1: RESUME
    # ==========================================

    pdf_path = input("\nEnter PDF path: ").strip()

    if not pdf_path:
        print("Please enter a PDF path.")
        return

    try:

        resume_result = process_resume(pdf_path)

        resume_text = resume_result["text"]
        resume_skills = resume_result["skills"]

        print("\nResume processed successfully!")

        # ==========================================
        # RESUME SKILLS
        # ==========================================

        print("\n" + "=" * 60)
        print("RESUME SKILLS")
        print("=" * 60)

        if resume_skills:

            for skill in resume_skills:
                print("✓", skill)

        else:

            print("No skills detected.")

        # ==========================================
        # STEP 2: JOB DESCRIPTION
        # ==========================================

        print("\n" + "=" * 60)
        print("JOB DESCRIPTION")
        print("=" * 60)

        print("Paste the Job Description below.")
        print("Type END on a new line when finished.\n")

        jd_lines = []

        while True:

            line = input()

            if line.strip().upper() == "END":
                break

            jd_lines.append(line)

        job_description = "\n".join(jd_lines)

        if not job_description.strip():

            print("Job Description cannot be empty.")
            return

        # ==========================================
        # STEP 3: JD ANALYSIS
        # ==========================================

        jd_result = analyze_job_description(job_description)

        required_skills = jd_result["required_skills"]

        print("\n" + "=" * 60)
        print("REQUIRED SKILLS")
        print("=" * 60)

        if required_skills:

            for skill in required_skills:
                print("•", skill)

        else:

            print("No required skills detected.")

        # ==========================================
        # STEP 4: SKILL MATCHING
        # ==========================================

        comparison = compare_resume_with_jd(
            resume_skills,
            required_skills
        )

        skill_match = comparison["match_percentage"]

        # ==========================================
        # STEP 5: NLP SIMILARITY
        # ==========================================

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # ==========================================
        # STEP 6: OVERALL SCORE
        # ==========================================

        overall_score = (
            (skill_match * 0.6) +
            (similarity_score * 0.4)
        )

        overall_score = round(overall_score, 2)

        # ==========================================
        # FINAL RESULT
        # ==========================================

        print("\n" + "=" * 60)
        print("              FINAL ANALYSIS")
        print("=" * 60)

        print(f"\nSkill Match Score : {skill_match}%")

        print(f"NLP Similarity    : {similarity_score}%")

        print(f"Overall Match     : {overall_score}%")

        # ==========================================
        # MATCHING SKILLS
        # ==========================================

        print("\n" + "=" * 60)
        print("MATCHING SKILLS")
        print("=" * 60)

        if comparison["matching_skills"]:

            for skill in comparison["matching_skills"]:
                print("✓", skill)

        else:

            print("No matching skills found.")

        # ==========================================
        # MISSING SKILLS
        # ==========================================

        print("\n" + "=" * 60)
        print("MISSING SKILLS")
        print("=" * 60)

        if comparison["missing_skills"]:

            for skill in comparison["missing_skills"]:
                print("✗", skill)

        else:

            print("No missing skills!")

        # ==========================================
        # RECOMMENDATION
        # ==========================================

        print("\n" + "=" * 60)
        print("RECOMMENDATION")
        print("=" * 60)

        if overall_score >= 80:

            print("Excellent match! Your resume strongly matches this job.")

        elif overall_score >= 60:

            print("Good match! Consider improving the missing skills.")

        elif overall_score >= 40:

            print("Moderate match. Your resume needs improvement.")

        else:

            print("Low match. Consider gaining more relevant skills.")

        print("\n" + "=" * 60)
        print("AI Resume Analysis Completed Successfully!")
        print("=" * 60)

    except FileNotFoundError:

        print("\nERROR: PDF file not found.")
        print("Please check the PDF path.")

    except Exception as e:

        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()