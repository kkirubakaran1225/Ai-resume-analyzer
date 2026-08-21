import re


def analyze_keywords(resume_text, job_description):

    resume_text = resume_text.lower()

    job_description = job_description.lower()

    # Extract words from JD
    jd_words = re.findall(
        r'\b[a-zA-Z][a-zA-Z0-9+#.-]{2,}\b',
        job_description
    )

    # Remove common English words
    stop_words = {

        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "are",
        "you",
        "your",
        "our",
        "from",
        "have",
        "has",
        "will",
        "should",
        "into",
        "about",
        "using",
        "work",
        "working",
        "experience",
        "years",
        "year",
        "job",
        "role",
        "candidate",
        "required",
        "requirements",
        "skills",
        "team",
        "good",
        "strong"

    }

    keywords = []

    for word in jd_words:

        if word not in stop_words:

            if word not in keywords:

                keywords.append(word)

    found_keywords = []

    missing_keywords = []

    for keyword in keywords:

        pattern = r'\b' + re.escape(keyword) + r'\b'

        if re.search(pattern, resume_text):

            found_keywords.append(keyword)

        else:

            missing_keywords.append(keyword)

    # Calculate keyword match

    if len(keywords) > 0:

        keyword_score = (
            len(found_keywords)
            /
            len(keywords)
        ) * 100

    else:

        keyword_score = 0

    return {

        "keywords": keywords,

        "found_keywords": found_keywords,

        "missing_keywords": missing_keywords,

        "keyword_score": round(
            keyword_score,
            2
        )

    }