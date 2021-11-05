def is_bangla_digit(char: chr) -> bool:
    """Checks if the given character is a digit in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a digit in Bangla, False otherwise.
    """
    return char in '০১২৩৪৫৬৭৮৯'


def is_bangla_pre_kar(char: chr) -> bool:
    """Checks if the given character is a pre sign (কার) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a pre kar in Bangla, False otherwise.
    """
    return char in ['ি', 'ে', 'ৈ']


def is_bangla_post_kar(char: chr) -> bool:
    """Checks if the given character is a post sign (কার) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a post kar in Bangla, False otherwise.
    """
    return char in ['া', 'ো', 'ৌ', 'ৗ', 'ু', 'ূ', 'ৃ', 'ী']


def is_bangla_kar(char: chr) -> bool:
    """Checks if the given character is a kar (কার) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a kar in Bangla, False otherwise.
    """
    return char in ['ি', 'ে', 'ৈ', 'া', 'ো', 'ৌ', 'ৗ', 'ু', 'ূ', 'ৃ', 'ী']


def is_bangla_vowel(char: chr) -> bool:
    """Checks if the given character is a vowel (স্বরবর্ণ) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a vowel in Bangla, False otherwise.
    """
    return char in ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']


def is_bangla_consonant(char: chr) -> bool:
    """Checks if the given character is a consonant (ব্যাঞ্জনবর্ণ) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a consonant in Bangla, False otherwise.
    """
    return char in ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ',
                    'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ',
                    'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ', 'ড়', 'ঢ়', 'য়', 'ং',
                    'ঃ', 'ঁ', 'ৎ']


def is_bangla_nukta(char: chr) -> bool:
    """Checks if the given character is a nukta (নুক্তা) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a nukta in Bangla, False otherwise.
    """
    return char in ['ং', 'ঃ', 'ঁ']

def is_bangla_halant(char: chr) -> bool:
    """Checks if the given character is a halant (হসন্ত) in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a halant in Bangla, False otherwise.
    """
    return char in ['্']

def is_bangla_fola(char: chr) -> bool:
    """Checks if the given character is a fola in Bangla.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a fola in Bangla, False otherwise.
    """
    return char in ['্য', '‍্র']

def is_space(char: chr) -> bool:
    """Check if the given character is a space.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a space, False otherwise.
    """
    return char in [' ', '\t', '\n', '\r']
