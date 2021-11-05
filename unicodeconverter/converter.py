from unicodeconverter.maps import *
from unicodeconverter.utils.rearrange import rearrange_unicode_text

def convert_bijoy_to_unicode(text: str) -> str:
    """Converts Bijoy text to Unicode.

    Args:
        text (str): Bijoy text to be converted.

    Returns:
        str: Converted Unicode text.
    """
    for bijoy_char, uni_char in bijoy_to_unicode.items():
        text = text.replace(bijoy_char, uni_char)
        
    text = rearrange_unicode_text(text)
    
    return text.strip()