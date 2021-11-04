def is_bangla_digit(char: chr) -> bool:
    return char in '০১২৩৪৫৬৭৮৯'


def is_bangla_pre_kar(char: chr) -> bool:
    return char in ['ি', 'ে', 'ৈ']


def is_bangla_post_kar(char: chr) -> bool:
    return char in ['া', 'ো', 'ৌ', 'ৗ', 'ু', 'ূ', 'ৃ', 'ী']


def is_bangla_kar(char: chr) -> bool:
    return char in ['ি', 'ে', 'ৈ', 'া', 'ো', 'ৌ', 'ৗ', 'ু', 'ূ', 'ৃ', 'ী']


def is_bangla_vowel(char: chr) -> bool:
    return char in ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']


def is_bangla_consonant(char: chr) -> bool:
    return char in ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ',
                    'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ',
                    'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ', 'ড়', 'ঢ়', 'য়', 'ং',
                    'ঃ', 'ঁ', 'ৎ']


def is_bangla_nukta(char: chr) -> bool:
    return char in ['ং', 'ঃ', 'ঁ']

def is_bangla_halant(char: chr) -> bool:
    return char in ['্']

def is_bangla_fola(char: chr) -> bool:
    return char in ['্য', '‍্র']

def is_space(char: chr) -> bool:
    return char in [' ', '\t', '\n', '\r']
