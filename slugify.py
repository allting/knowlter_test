"""Utilities for turning text into URL-friendly slugs."""


def slugify(text: str) -> str:
    """Convert *text* to a lowercase slug separated by single hyphens."""
    if not text:
        raise ValueError("text must not be empty")

    parts = []
    pending_separator = False
    for character in text:
        if character.isalnum():
            if pending_separator and parts:
                parts.append("-")
            parts.append(character.lower())
            pending_separator = False
        else:
            pending_separator = True

    result = "".join(parts)
    if not result:
        raise ValueError("text must contain at least one alphanumeric character")
    return result
