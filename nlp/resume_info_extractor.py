import re


# ============================================================
# SECTION HEADINGS
# ============================================================

SECTION_NAMES = {
    "summary": [
        "professional summary",
        "profile summary",
        "career summary",
        "summary",
        "profile",
        "objective",
        "career objective"
    ],

    "skills": [
        "technical skills",
        "skills",
        "technical skill",
        "skill set"
    ],

    "education": [
        "education",
        "academic background",
        "educational qualification",
        "academic qualifications"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "project experience"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "certification"
    ],

    "achievements": [
        "achievements",
        "awards",
        "accomplishments"
    ],

    "languages": [
        "languages",
        "language"
    ]
}


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):

    if not text:
        return ""

    text = text.replace("\r", "\n")

    # Remove excessive spaces
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove excessive blank lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()


# ============================================================
# FIND SECTION
# ============================================================

def find_section(text, section_type):

    if section_type not in SECTION_NAMES:
        return ""

    names = SECTION_NAMES[section_type]

    # Create heading pattern
    pattern = "|".join(
        re.escape(name)
        for name in names
    )

    # Look for heading
    match = re.search(
        rf'(?im)(?:^|\n)\s*(?:{pattern})\s*:?\s*(?:\n|$)',
        text
    )

    if not match:

        # PDF may not preserve new lines.
        # Try searching anywhere in text.
        match = re.search(
            rf'(?i)\b(?:{pattern})\b\s*:?\s*',
            text
        )

        if not match:
            return ""

    start = match.end()

    # Find next section
    remaining_text = text[start:]

    next_sections = []

    for names_list in SECTION_NAMES.values():

        for name in names_list:

            next_sections.append(
                re.escape(name)
            )

    next_pattern = "|".join(next_sections)

    next_match = re.search(
        rf'(?im)\b(?:{next_pattern})\b\s*:?\s*',
        remaining_text
    )

    if next_match:

        section_text = remaining_text[
            :next_match.start()
        ]

    else:

        section_text = remaining_text

    return section_text.strip()


# ============================================================
# CLEAN SECTION
# ============================================================

def clean_section(text):

    if not text:
        return ""

    # Replace bullets with newline
    text = re.sub(
        r'[•●▪◦]',
        '\n',
        text
    )

    # Try to separate common resume patterns
    text = re.sub(
        r'\s+(?=[A-Z][A-Za-z ]{2,30}\s*[-|:])',
        '\n',
        text
    )

    # Clean spaces
    text = re.sub(
        r'[ \t]+',
        ' ',
        text
    )

    # Clean blank lines
    text = re.sub(
        r'\n+',
        '\n',
        text
    )

    return text.strip()


# ============================================================
# CONVERT SECTION TO LIST
# ============================================================

def section_to_list(text):

    if not text:
        return []

    text = clean_section(text)

    lines = text.split("\n")

    results = []

    for line in lines:

        line = line.strip()

        if len(line) < 3:
            continue

        if line not in results:

            results.append(line)

    return results[:10]


# ============================================================
# EMAIL
# ============================================================

def extract_email(text):

    match = re.search(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        text
    )

    if match:

        return match.group(0)

    return None


# ============================================================
# PHONE
# ============================================================

def extract_phone(text):

    # Indian phone number
    match = re.search(
        r'(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)',
        text
    )

    if match:

        return match.group(0)

    return None


# ============================================================
# LINKEDIN
# ============================================================

def extract_linkedin(text):

    match = re.search(
        r'(https?://)?(www\.)?linkedin\.com/[^\s]+',
        text,
        re.IGNORECASE
    )

    if match:

        return match.group(0)

    return None


# ============================================================
# GITHUB
# ============================================================

def extract_github(text):

    match = re.search(
        r'(https?://)?(www\.)?github\.com/[^\s]+',
        text,
        re.IGNORECASE
    )

    if match:

        return match.group(0)

    return None


# ============================================================
# MAIN FUNCTION
# ============================================================

def extract_resume_information(text):

    if not text:

        return {
            "email": None,
            "phone": None,
            "linkedin": None,
            "github": None,
            "education": [],
            "experience": [],
            "projects": []
        }


    # Normalize
    text = normalize_text(text)


    # ========================================================
    # CONTACT INFORMATION
    # ========================================================

    email = extract_email(text)

    phone = extract_phone(text)

    linkedin = extract_linkedin(text)

    github = extract_github(text)


    # ========================================================
    # EXTRACT SECTIONS
    # ========================================================

    education_text = find_section(
        text,
        "education"
    )

    experience_text = find_section(
        text,
        "experience"
    )

    projects_text = find_section(
        text,
        "projects"
    )


    # ========================================================
    # CONVERT TO LIST
    # ========================================================

    education = section_to_list(
        education_text
    )

    experience = section_to_list(
        experience_text
    )

    projects = section_to_list(
        projects_text
    )


    # ========================================================
    # FALLBACK EDUCATION
    # ========================================================

    if not education:

        education_keywords = [
            "b.e",
            "b.tech",
            "mca",
            "m.tech",
            "bca",
            "b.sc",
            "m.sc",
            "bachelor",
            "master",
            "university",
            "college"
        ]

        for line in text.split("\n"):

            lower_line = line.lower()

            if any(
                keyword in lower_line
                for keyword in education_keywords
            ):

                if line.strip() not in education:

                    education.append(
                        line.strip()
                    )


    # ========================================================
    # RETURN RESULT
    # ========================================================

    return {

        "email": email,

        "phone": phone,

        "linkedin": linkedin,

        "github": github,

        "education": education[:10],

        "experience": experience[:10],

        "projects": projects[:10]

    }