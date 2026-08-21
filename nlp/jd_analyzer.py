from .text_cleaner import clean_text
from .skill_extractor import extract_skills
from .skill_mapping import find_related_skills


def analyze_job_description(job_description):

    # Clean the job description
    cleaned_jd = clean_text(job_description)

    # Extract required skills
    required_skills = extract_skills(cleaned_jd)

    return {
        "job_description": cleaned_jd,
        "required_skills": required_skills
    }


def compare_resume_with_jd(resume_skills, required_skills):

    # Convert everything to lowercase
    resume_skills = set(
        skill.lower().strip()
        for skill in resume_skills
    )

    required_skills = set(
        skill.lower().strip()
        for skill in required_skills
    )

    # ==========================================
    # EXACT MATCHING
    # ==========================================

    exact_matches = resume_skills.intersection(
        required_skills
    )

    # ==========================================
    # SMART RELATED-SKILL MATCHING
    # ==========================================

    smart_matches = set()

    for required_skill in required_skills:

        # Get related skills
        related_skills = find_related_skills(
            required_skill
        )

        # Check whether resume contains
        # any related skill
        if resume_skills.intersection(
            related_skills
        ):

            smart_matches.add(required_skill)

    # Combine exact + smart matches
    matching_skills = exact_matches.union(
        smart_matches
    )

    # ==========================================
    # MISSING SKILLS
    # ==========================================

    missing_skills = required_skills.difference(
        matching_skills
    )

    # ==========================================
    # MATCH PERCENTAGE
    # ==========================================

    if len(required_skills) > 0:

        match_percentage = (
            len(matching_skills)
            /
            len(required_skills)
        ) * 100

    else:

        match_percentage = 0

    return {

        "matching_skills":
            sorted(matching_skills),

        "missing_skills":
            sorted(missing_skills),

        "match_percentage":
            round(match_percentage, 2)

    }