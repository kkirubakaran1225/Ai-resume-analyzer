import re


# ============================================================
# SKILL DATABASE
# ============================================================

SKILLS = [

    # ---------------- PYTHON ----------------

    "python",
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "nltk",
    "spacy",
    "streamlit",
    "fastapi",
    "flask",
    "django",

    # ---------------- JAVA ----------------

    "java",
    "spring",
    "spring boot",
    "hibernate",
    "maven",
    "gradle",

    # ---------------- C / C++ ----------------

    "c",
    "c++",
    "c#",
    ".net",
    "asp.net",
    ".net core",

    # ---------------- WEB DEVELOPMENT ----------------

    "html",
    "css",
    "javascript",
    "typescript",
    "react",
    "angular",
    "vue",
    "node.js",
    "express",
    "bootstrap",
    "jquery",

    # ---------------- DATABASE ----------------

    "sql",
    "mysql",
    "postgresql",
    "oracle",
    "pl/sql",
    "mongodb",
    "sqlite",
    "redis",
    "mariadb",
    "sql server",

    # ---------------- DATA ANALYTICS ----------------

    "power bi",
    "tableau",
    "excel",
    "data analysis",
    "data visualization",
    "statistics",
    "data analytics",

    # ---------------- AI / MACHINE LEARNING ----------------

    "artificial intelligence",
    "machine learning",
    "deep learning",
    "natural language processing",
    "computer vision",
    "nlp",
    "llm",
    "generative ai",

    # ---------------- CLOUD ----------------

    "aws",
    "amazon web services",
    "azure",
    "google cloud",
    "gcp",
    "cloud computing",

    # ---------------- DEVOPS ----------------

    "docker",
    "kubernetes",
    "jenkins",
    "ci/cd",
    "terraform",
    "ansible",

    # ---------------- VERSION CONTROL ----------------

    "git",
    "github",
    "gitlab",
    "bitbucket",

    # ---------------- OPERATING SYSTEM ----------------

    "linux",
    "ubuntu",
    "windows",
    "centos",

    # ---------------- BIG DATA ----------------

    "hadoop",
    "spark",
    "apache spark",
    "hive",
    "kafka",

    # ---------------- TESTING ----------------

    "selenium",
    "pytest",
    "junit",
    "postman",
    "unit testing",

    # ---------------- SOFTWARE ENGINEERING ----------------

    "rest api",
    "restful api",
    "api",
    "microservices",
    "object oriented programming",
    "oops",
    "data structures",
    "algorithms",

    # ---------------- OTHER ----------------

    "jira",
    "agile",
    "scrum",
    "communication",
    "problem solving"
]


# ============================================================
# SKILL EXTRACTION FUNCTION
# ============================================================

def extract_skills(text):

    if not text:
        return []

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special regex characters
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(set(found_skills))