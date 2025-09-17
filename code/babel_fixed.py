"""
This script demonstrates the limitations of Babel's negotiate_locale() function
when handling Accept-Language headers with quality values (q=). It provides
a manual parsing and negotiation approach to correctly respect quality values,
as well as a preprocessing step to make Babel work better in this context.
"""
from babel import Locale
from babel.core import negotiate_locale
import re

def parse_accept_language(accept_language_header):
    """
    Properly parse Accept-Language header with quality values
    """
    if not accept_language_header:
        return []
    
    languages = []
    for item in accept_language_header.split(','):
        item = item.strip()
        
        if ';q=' in item:
            lang, quality = item.split(';q=', 1)
            try:
                quality = float(quality)
            except ValueError:
                quality = 1.0
        else:
            lang = item
            quality = 1.0
        
        lang = lang.strip()
        languages.append((lang, quality))
    
    # Sort by quality (highest first)
    languages.sort(key=lambda x: x[1], reverse=True)
    return languages

def manual_language_negotiation(accept_language_header, available_languages):
    """
    Manual language negotiation that respects quality values
    """
    parsed_langs = parse_accept_language(accept_language_header)
    
    for lang, quality in parsed_langs:
        # Try exact match first
        if lang in available_languages:
            return lang
        
        # Try with country code removed (e.g., es-ES -> es)
        if '-' in lang:
            base_lang = lang.split('-')[0]
            if base_lang in available_languages:
                return base_lang
        
        # Try wildcard match
        if lang == '*' and available_languages:
            return available_languages[0]
    
    return None

def babel_with_preprocessing(accept_language_header, available_languages):
    """
    Use Babel but preprocess the header to work around its limitations
    """
    # Parse and extract just the language codes, ordered by quality
    parsed_langs = parse_accept_language(accept_language_header)
    
    # Create a simplified header for Babel (remove quality values)
    simplified_langs = [lang for lang, quality in parsed_langs if lang != '*']
    
    if not simplified_langs:
        return None
    
    # Try negotiate_locale with individual languages
    for lang, quality in parsed_langs:
        if lang == '*':
            continue
            
        # Try with just this language
        result = negotiate_locale([lang], available_languages, sep='-')
        if result:
            return result
    
    return None

# Test the different approaches
print("=== TESTING DIFFERENT APPROACHES ===")
accept_header = "en;q=0.7, es-ES, fr-FR;q=0.8"
available_langs = ['en', 'fr', 'de', 'es']

print(f"Accept-Language: {accept_header}")
print(f"Available languages: {available_langs}")
print()

# 1. Original Babel approach (problematic)
print("1. Original Babel negotiate_locale:")
original_result = negotiate_locale([accept_header], available_langs, sep='-')
print(f"   Result: {original_result}")
print()

# 2. Manual parsing and negotiation
print("2. Manual language negotiation:")
manual_result = manual_language_negotiation(accept_header, available_langs)
print(f"   Result: {manual_result}")
print()

# 3. Babel with preprocessing
print("3. Babel with preprocessing:")
babel_result = babel_with_preprocessing(accept_header, available_langs)
print(f"   Result: {babel_result}")
print()

# 4. Show parsed preferences
print("4. Parsed language preferences:")
parsed = parse_accept_language(accept_header)
for i, (lang, quality) in enumerate(parsed, 1):
    print(f"   {i}. {lang} (q={quality})")
print()

# Test with different headers
test_headers = [
    "en-US,en;q=0.9,fr;q=0.8,de;q=0.7",
    "fr-CA,fr;q=0.8,en-US;q=0.6,en;q=0.4", 
    "es-ES,es;q=0.9,en;q=0.8",
    "de,en;q=0.5",
    "*;q=0.1"
]

print("=== TESTING MULTIPLE HEADERS ===")
for header in test_headers:
    print(f"\nHeader: {header}")
    
    manual = manual_language_negotiation(header, available_langs)
    babel_prep = babel_with_preprocessing(header, available_langs)
    
    print(f"  Manual negotiation: {manual}")
    print(f"  Babel preprocessed: {babel_prep}")

def explain_babel_limitations():
    """
    Explain why Babel's negotiate_locale fails with quality values
    """
    print("\n=== WHY BABEL FAILS ===")
    print("Babel's negotiate_locale() has these limitations:")
    print("1. It expects a list of individual language codes, not a full Accept-Language header")
    print("2. It doesn't parse quality values (q=0.7) - it treats the whole string as one language")
    print("3. When it can't parse 'en;q=0.7, es-ES, fr-FR;q=0.8' as a valid locale, it returns None")
    print()
    print("CORRECT usage of negotiate_locale:")
    
    # Show correct usage
    languages_list = ['en', 'es-ES', 'fr-FR']  # Individual languages
    result = negotiate_locale(languages_list, available_langs, sep='-')
    print(f"  negotiate_locale({languages_list}, {available_langs}) = {result}")

explain_babel_limitations()
