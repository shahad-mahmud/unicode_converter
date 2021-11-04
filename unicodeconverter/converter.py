from maps import *
from utils.rearrange import rearrange_unicode_text

class UnicodeConverter:
    def __init__(self):
        pass
    
    @staticmethod
    def from_bijoy(text: str) -> str:
        for bijoy_char, uni_char in bijoy_to_unicode.items():
            text = text.replace(bijoy_char, uni_char)
            
        text = rearrange_unicode_text(text)
        
        return text