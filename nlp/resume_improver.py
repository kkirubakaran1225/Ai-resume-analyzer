def generate_improvement_suggestions(
    missing_skills,
    ats_suggestions,
    overall_score
):

    suggestions = []

    # ==========================================
    # MISSING SKILLS
    # ==========================================

    if missing_skills:

        for skill in missing_skills[:5]:

            suggestions.append(
                f"Consider adding '{skill}' to your "
                f"resume if you have relevant experience."
            )

    # ==========================================
    # ATS SUGGESTIONS
    # ==========================================

    if ats_suggestions:

        for suggestion in ats_suggestions:

            suggestions.append(suggestion)

    # ==========================================
    # SCORE BASED SUGGESTIONS
    # ==========================================

    if overall_score < 40:

        suggestions.append(
            "Your resume has a low match score. "
            "Review the job description and highlight "
            "your most relevant skills and projects."
        )

    elif overall_score < 60:

        suggestions.append(
            "Your resume has a moderate match. "
            "Focus on the missing skills and relevant "
            "job-specific keywords."
        )

    elif overall_score < 80:

        suggestions.append(
            "Your resume is a good match. "
            "Strengthen your missing skills and "
            "add measurable achievements."
        )

    else:

        suggestions.append(
            "Your resume is a strong match. "
            "Keep the content concise and ATS-friendly."
        )

    # ==========================================
    # GENERAL RESUME TIPS
    # ==========================================

    suggestions.append(
        "Use measurable achievements in your "
        "experience and project descriptions."
    )

    suggestions.append(
        "Use clear section headings such as "
        "Skills, Education, Experience and Projects."
    )

    suggestions.append(
        "Avoid unnecessary graphics, tables and "
        "complex formatting for ATS compatibility."
    )

    return suggestions