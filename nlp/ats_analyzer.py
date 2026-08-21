import re


def analyze_ats(resume_text):

    text = resume_text.lower()

    sections = {
        "contact": False,
        "summary": False,
        "education": False,
        "skills": False,
        "experience": False,
        "projects": False
    }

    # Contact information
    if re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text):
        sections["contact"] = True

    # Section keywords
    section_keywords = {
        "summary": [
            "summary",
            "professional summary",
            "profile",
            "objective"
        ],

        "education": [
            "education",
            "academic",
            "qualification"
        ],

        "skills": [
            "skills",
            "technical skills",
            "technologies"
        ],

        "experience": [
            "experience",
            "work experience",
            "employment"
        ],

        "projects": [
            "projects",
            "academic projects",
            "personal projects"
        ]
    }

    for section, keywords in section_keywords.items():

        for keyword in keywords:

            if keyword in text:
                sections[section] = True
                break

    # Calculate section score
    total_sections = len(sections)

    completed_sections = sum(
        sections.values()
    )

    section_score = (
        completed_sections / total_sections
    ) * 100

    # Suggestions
    suggestions = []

    for section, exists in sections.items():

        if not exists:

            suggestions.append(
                f"Consider adding a {section} section."
            )

    return {
        "sections": sections,
        "section_score": round(section_score, 2),
        "suggestions": suggestions
    }