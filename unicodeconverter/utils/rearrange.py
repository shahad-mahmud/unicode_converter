from unicodeconverter.utils.checkers import *


def rearrange_unicode_text(text: str):
    for i in range(len(text)):
        # handle hasanta
        if is_bangla_halant(text[i]) and i < len(text) - 1:
            
            if (is_bangla_kar(text[i - 1]) or is_bangla_nukta(text[i - 1])):
                temp_text = text[:i - 1]
                temp_text += text[i]
                temp_text += text[i + 1]
                temp_text += text[i - 1]
                temp_text += text[i + 2:]
                
                text = temp_text
            
            if text[i-1] == 'র' and not is_bangla_halant(text[i-2]) and is_bangla_kar(text[i+1]):
                temp_text = text[:i - 1]
                temp_text += text[i + 1]
                temp_text += text[i - 1]
                temp_text += text[i]
                temp_text += text[i + 2:]
                
                text = temp_text
                
        if text[i] == 'র'  and is_bangla_halant(text[i + 1]) and not is_bangla_halant(text[i-1]) and i < len(text) - 1:
            j = 1
            
            while True:
                if i - j < 0:
                    break                
                if is_bangla_consonant(text[i - j]) and not is_bangla_halant(text[i - j - 1]):
                    j += 2
                elif j ==1 and is_bangla_kar(text[i - j]):
                    j += 1
                else:
                    break
            
            temp_text = text[:i - j]
            temp_text += text[i]
            temp_text += text[i + 1]
            temp_text += text[i - j: i]
            temp_text += text[i + 2:]
            
            text = temp_text
            i += 1
            continue
        
        if not (is_bangla_pre_kar(text[i]) and is_space(text[i+1]) and i < len(text) - 1):
            temp_text = text[:i]
            j = 1
            
            while is_bangla_consonant(text[i + j]):
                if is_bangla_halant(text[i + j + 1]):
                    j += 2
                else:
                    break
                
            temp_text += text[i + 1 : i + j + 1]
            k = 0
            if text[i] == 'ে':
                if text[i + j + 1] == 'া':
                    temp_text += 'ো'
                    k = 1
                elif text[i + j + 1] == 'ৗ':
                    temp_text += 'ৌ'
                    k = 1
            else:
                temp_text += text[i]
            
            temp_text += text[i + j + k + 1:]
            text = temp_text
            i += j
            
        if text[i] == 'ঁ' and is_bangla_post_kar(text[i + 1]) and i < len(text) - 1:
            temp_text = text[:i]
            temp_text += text[i + 1]
            temp_text += text[i]
            temp_text += text[i + 2:]
            
            text = temp_text
            
        return text
            
        
        
