from unicodeconverter.utils.checkers import *


def rearrange_unicode_text(text: str):
    i = 0
    # for ch in text:
    #     print(ch)
    while i < len(text):
        # print(i, text[i], text)
        # handle hasanta
        if is_bangla_halant(text[i]) and i < len(text) - 1:
            
            if (is_bangla_kar(text[i - 1]) or is_bangla_nukta(text[i - 1])):
                # print('hasanta - nukta')
                temp_text = text[:i - 1]
                temp_text += text[i]
                temp_text += text[i + 1]
                temp_text += text[i - 1]
                temp_text += text[i + 2:]
                
                text = temp_text
            
            if text[i-1] == 'র' and not is_bangla_halant(text[i-2]) and is_bangla_kar(text[i+1]):
                # print('hasanta - ro')
                temp_text = text[:i - 1]
                temp_text += text[i + 1]
                temp_text += text[i - 1]
                temp_text += text[i]
                temp_text += text[i + 2:]
                
                text = temp_text
                
        if text[i] == 'র'  and is_bangla_halant(text[i + 1]) and not is_bangla_halant(text[i-1]) and i < len(text) - 1:
            # print('only ro')
            j = 1
            
            while True:
                if i - j < 0:
                    break                
                if is_bangla_consonant(text[i - j]) and is_bangla_halant(text[i - j - 1]):
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
            i += 2
            continue
        
        if is_bangla_pre_kar(text[i]) and not is_space(text[i+1]) and i < len(text) - 1:
            # print('pre_kar - space false')
            temp_text = text[:i]
            j = 1
            
            while is_bangla_consonant(text[i + j]):
                if is_bangla_halant(text[i + j + 1]):
                    j += 2
                else:
                    break
                
            temp_text += text[i + 1 : i + j + 1]
            # print('after sonsonent', temp_text)
            k = 0
            if text[i] == 'ে' and text[i + j + 1] == 'া':
                temp_text += 'ো'
                k = 1
            elif text[i] == 'ে' and text[i + j + 1] == 'ৗ':
                temp_text += 'ৌ'
                k = 1
            else:
                temp_text += text[i]
            
            temp_text += text[i + j + k + 1:]
            # print('after e-ker lookup', temp_text)
            text = temp_text
            i += j
            
        if text[i] == 'ঁ' and is_bangla_post_kar(text[i + 1]) and i < len(text) - 1:
            # print('chondra')
            temp_text = text[:i]
            temp_text += text[i + 1]
            temp_text += text[i]
            temp_text += text[i + 2:]
            
            text = temp_text
        i += 1
           
    return text
            
        
        
