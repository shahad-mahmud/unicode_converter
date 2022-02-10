import re
import string
from unicodeconverter.maps import *
from unicodeconverter.utils.rearrange import rearrange_bijoy_text, rearrange_unicode_text

def convert_bijoy_to_unicode(text: str) -> str:
    """Converts Bijoy text to Unicode.

    Args:
        text (str): Bijoy text to be converted.

    Returns:
        str: Converted Unicode text.
    """
    # Handle punctuations
    text = re.sub('([.,!?();:-])', r'\t\1', text)
    text = re.sub('[\r\t\f\v  ]{2,}', ' ', text)
    
    # Handle new lines
    text = text.replace('\n', '\t\n')
    
    # Handle multiple char tokens
    for pre_pattern, post_pattern in bijoy_pre_map.items():
        text = text.replace(pre_pattern, post_pattern)
    
    # Segmentation    
    for bijoy_char, _ in bijoy_to_unicode.items():
        text = text.replace(bijoy_char, f'\t{bijoy_char}')
    
    rearranged_bijoy_text = rearrange_bijoy_text(text.strip())
    
    # Convert to Unicode
    for bijoy_char, uni_char in bijoy_to_unicode.items():
        rearranged_bijoy_text = rearranged_bijoy_text.replace(bijoy_char, uni_char)
        
    return rearranged_bijoy_text.strip()