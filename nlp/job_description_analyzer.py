from .text_cleaner import clean_text
kk
from .skill_extractor import extract_skills


def analyze_job_description(job_description):
    # Clean the job description
    cleaned_jd = clean_text(job_description)

    # Extract skills from the job description
    required_skills = extract_skills(cleaned_jd)

    return {
        "job_description": cleaned_jd,
        "required_skills": required_skills
    }


def compare_resume_with_jd(resume_skills, required_skills):
    resume_skills = set(skill.lower() for skill in resume_skills)
    required_skills = set(skill.lower() for skill in required_skills)

    matching_skills = resume_skills.intersection(required_skills)
    missing_skills = required_skills.difference(resume_skills)

    if len(required_skills) > 0:
        match_percentage = (
            len(matching_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0

    return {
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills),
        "match_percentage": round(match_percentage, 2)
    }