# python
"""
unicodedata.normalize('NFKC', text)
Applies Unicode Normalization Form KC (compatibility decomposition followed by canonical composition). This:
Maps compatibility characters to their canonical equivalents (e.g., ligatures like ﬀ → ff, fullwidth Ｆ → F, superscripts, etc.).
Decomposes then recomposes combining sequences so visually identical strings use the same codepoints (e.g., e\u0301 → é).
Makes comparisons, storage, and searching more reliable.
.strip()
Removes leading and trailing whitespace (all Unicode whitespace characters where str.isspace() is true).
Order matters: normalizing first can convert visually-space-like characters (fullwidth space, some compatibility spaces) into forms that .strip() will remove.

"""
import unicodedata

cases = [
    "  example  ",
    "\u3000fullwidth space\u3000",      # U+3000 IDEOGRAPHIC SPACE
    "e\u0301",                          # 'e' + combining acute
    "\ufb00abc\ufb01",                  # ligatures: ﬀ, ﬁ
]

for s in cases:
    normalized = unicodedata.normalize("NFKC", s)
    trimmed = normalized.strip()
    print(repr(s), "→", repr(normalized), "→", repr(trimmed))
