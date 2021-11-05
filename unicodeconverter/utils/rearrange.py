from unicodeconverter.utils.checkers import *


def rearrange_unicode_text(text: str) -> str:
    """Rearrange the Bijoy to Unicode mapped characters and 
    create the desired Unicode text.

    Args:
        text (str): Bijoy to Unicode mapped text.

    Returns:
        str: Arranged Unicode text.
    """
    i = 0
    while i < len(text):
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

        # Handle ref (রেফ)
        if text[i] == 'র' and is_bangla_halant(text[i + 1]) and not is_bangla_halant(text[i-1]) and i < len(text) - 1:
            j = 1

            while True:
                if i - j < 0:
                    break
                if is_bangla_consonant(text[i - j]) and is_bangla_halant(text[i - j - 1]):
                    j += 2
                elif j == 1 and is_bangla_kar(text[i - j]):
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
            temp_text = text[:i]
            j = 1

            while is_bangla_consonant(text[i + j]):
                if is_bangla_halant(text[i + j + 1]):
                    j += 2
                else:
                    break

            temp_text += text[i + 1: i + j + 1]
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
            text = temp_text
            i += j

        if text[i] == 'ঁ' and is_bangla_post_kar(text[i + 1]) and i < len(text) - 1:
            temp_text = text[:i]
            temp_text += text[i + 1]
            temp_text += text[i]
            temp_text += text[i + 2:]

            text = temp_text
        i += 1

    return text
