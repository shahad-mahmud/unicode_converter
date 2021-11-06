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

    regex_pattern = re.compile(',')
    text = re.sub(regex_pattern, handle_punc, text)
    # print('TEXT AFTER REGEX:', text)
    # [!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]+
    # print(text)
    for bijoy_char, uni_char in bijoy_to_unicode.items():
        # text = text.replace(bijoy_char, uni_char)
        # print(f'bijoy: {bijoy_char}')
        text = text.replace(bijoy_char, f'\t{bijoy_char}')
        # print(text)
        # print()
    
    # print('TAB TEXT:', text)    
    # text = rearrange_unicode_text(text)
    bij = rearrange_bijoy_text(text.strip())
    # print(bij)
    
    for bijoy_char, uni_char in bijoy_to_unicode.items():
        # text = text.replace(bijoy_char, uni_char)
        bij = bij.replace(bijoy_char, uni_char)
    
    # print(bij)
    
    return bij.strip()

def handle_punc(m):
    return f'\t{m.group(0)}'