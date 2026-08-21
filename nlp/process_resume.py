from .resume_parser import extract_text_from_pdf
from .text_cleaner import clean_text
from .skill_extractor import extract_skills


def process_resume(pdf_path):
    # Extract text from PDF
    raw_text = extract_text_from_pdf(pdf_path)

    # Clean extracted text
    cleaned_text = clean_text(raw_text)

    # Extract skills
    skills = extract_skills(cleaned_text)

    return {
        "text": cleaned_text,
        "skills": skills
    }