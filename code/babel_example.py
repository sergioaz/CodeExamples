"""
Example of processing Accept-Language header using Babel - cannot handle quality values properly.
"""
from babel import Locale
from babel.core import negotiate_locale


def process_accept_language(accept_language_header, available_languages):
    """
    Process Accept-Language header using Babel
    """
    # Parse the header and negotiate the best language
    best_language = negotiate_locale(
        preferred=[accept_language_header],
        available=available_languages,
        sep='-'
    )

    return best_language


# Example usage
#accept_header = "en-US,en;q=0.9,fr;q=0.8,de;q=0.7"
#accept_header = "fr-CA,fr;q=0.8,en-US;q=0.6,en;q=0.4"
accept_header = "en;q=0.7, es-ES, fr-FR;q=0.8"
available_langs = ['en', 'fr', 'de', 'es']

best_lang = process_accept_language(accept_header, available_langs)
print(f"Best language: {best_lang}")

# More detailed example
from babel.localedata import locale_identifiers
from babel.core import parse_locale


def detailed_language_processing(accept_language_header):
    # Parse individual language preferences
    preferences = []

    # Simple parsing (you might want to use a more robust parser)
    for lang_part in accept_language_header.split(','):
        lang_part = lang_part.strip()
        if ';q=' in lang_part:
            lang, quality = lang_part.split(';q=')
            quality = float(quality)
        else:
            lang = lang_part
            quality = 1.0

        preferences.append((lang.strip(), quality))

    # Sort by quality (highest first)
    preferences.sort(key=lambda x: x[1], reverse=True)

    return preferences


# Example
header = "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,*;q=0.5"
prefs = detailed_language_processing(header)
print("Language preferences:", prefs)