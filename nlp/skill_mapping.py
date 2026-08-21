# Related skills and technology groups

SKILL_GROUPS = {

    "python": {
        "python",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "matplotlib"
    },

    "machine learning": {
        "machine learning",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "pandas",
        "numpy"
    },

    "data science": {
        "data science",
        "python",
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib"
    },

    "database": {
        "database",
        "mysql",
        "postgresql",
        "oracle",
        "sql",
        "mongodb",
        "sqlite"
    },

    "sql": {
        "sql",
        "mysql",
        "postgresql",
        "oracle",
        "pl/sql",
        "sqlite"
    },

    "frontend": {
        "html",
        "css",
        "javascript",
        "react",
        "angular",
        "vue",
        "bootstrap"
    },

    "backend": {
        "python",
        "java",
        "c#",
        "node.js",
        "php",
        "django",
        "flask",
        "spring"
    },

    "web development": {
        "html",
        "css",
        "javascript",
        "react",
        "angular",
        "node.js",
        "django",
        "flask",
        "php"
    },

    "cloud": {
        "aws",
        "azure",
        "google cloud",
        "gcp",
        "docker",
        "kubernetes"
    },

    "devops": {
        "docker",
        "kubernetes",
        "jenkins",
        "git",
        "github",
        "aws",
        "azure"
    },

    "version control": {
        "git",
        "github",
        "gitlab",
        "bitbucket"
    }
}


def find_related_skills(skill):

    skill = skill.lower().strip()

    related_skills = set()

    for group_name, skills in SKILL_GROUPS.items():

        if skill == group_name or skill in skills:

            related_skills.update(skills)

    return related_skills