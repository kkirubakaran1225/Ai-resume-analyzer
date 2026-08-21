import re


SKILLS = [
    "python",
    "java",
    "sql",
    "mysql",
    "oracle",
    "plsql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "github",
    "aws",
    "azure",
    "docker",
    "linux"
]


def extract_resume_skills(resume_text):

    resume_text = resume_text.lower()

    found_skills = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", resume_text):
            found_skills.append(skill)

    return found_skills


if __name__ == "__main__":

    resume_text = input("Paste extracted resume text:\n")

    skills = extract_resume_skills(resume_text)

    print("\n===== RESUME SKILLS =====")

    for skill in skills:
        print("✓", skill)