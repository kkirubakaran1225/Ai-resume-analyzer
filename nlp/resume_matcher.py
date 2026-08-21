from job_description_analyzer import analyze_job_description


def match_resume_with_job(resume_skills, job_description):

    jd_skills = analyze_job_description(job_description)

    matching_skills = []
    missing_skills = []

    for skill in jd_skills:
        if skill in resume_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(jd_skills) > 0:
        match_score = (len(matching_skills) / len(jd_skills)) * 100
    else:
        match_score = 0

    return matching_skills, missing_skills, match_score


if __name__ == "__main__":

    print("===== RESUME vs JOB DESCRIPTION =====")

    resume_skills = [
        "python",
        "sql",
        "mysql",
        "pandas",
        "git"
    ]

    job_description = input("\nPaste Job Description:\n")

    matching, missing, score = match_resume_with_job(
        resume_skills,
        job_description
    )

    print("\n===== RESULT =====")

    print("\nMatching Skills:")
    for skill in matching:
        print("✓", skill)

    print("\nMissing Skills:")
    for skill in missing:
        print("✗", skill)

    print(f"\nResume Match Score: {score:.2f}%")