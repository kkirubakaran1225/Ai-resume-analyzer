import re


def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces and new lines
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary special characters
    text = re.sub(r"[^a-zA-Z0-9\s.,@+#-]", "", text)

    return text.strip()