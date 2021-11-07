from unicodeconverter.utils.checkers import *
from unicodeconverter import lists


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


def rearrange_bijoy_text(text: str) -> str:
    """Rearrange the Bijoy characters to convert to Unicode directly

    Args:
        text (str): The bijoy text to be rearranged.

    Returns:
        str: The rearranged bijoy text.
    """
    segments = text.split('\t')
    n_segments = len(segments)

    i = 0
    while i < n_segments:
        if segments[i] == '':
            del segments[i]
            n_segments -= 1
            continue
        if segments[i] == '›':
            segments[i] = segments[i] + segments[i + 1]
            del segments[i + 1]
            n_segments -= 1
        i += 1

    i = 0
    while i < (len(segments)):
        if segments[i] == '‡' or segments[i] == "†":
            # handle o-kar and ou-kar
            if i < len(segments) - 2 and segments[i+2] == 'v':
                segments[i], segments[i+1] = segments[i+1], segments[i]
                i += 2
            elif i < len(segments) - 2 and segments[i+2] == 'Š':
                segments[i], segments[i+1] = segments[i+1], segments[i]
                i += 2
            else:
                # Handle e-kar
                j = 1
                if i + 2 < len(segments):
                    # Handle ref
                    if segments[i + 2] == '©':
                        segments[i], segments[i+2] = segments[i+2], segments[i]
                        i += 3
                        continue
                    # handle fola
                    if segments[i + j + 1] in lists.bijoy_fola:
                        j += 1

                for k in range(j):
                    segments[i + k], segments[i + k +
                                              1] = segments[i+k+1], segments[i+k]
                i += j
        # handle all kars
        elif segments[i] in lists.bijoy_pre_kars and i < len(segments) - 1:
            j = 1
            if i + 2 < len(segments):
                # check if next character is a ref
                if segments[i + 2] == '©':
                    segments[i], segments[i+2] = segments[i+2], segments[i]
                    i += 3
                    continue

                # check if the next character is a fola
                if segments[i + j + 1] in lists.bijoy_fola:
                    j += 1

            for k in range(j):
                segments[i + k], segments[i + k +
                                          1] = segments[i+k+1], segments[i+k]
            i += j
        # Handle ref
        elif segments[i] == '©':
            segments[i], segments[i-1] = segments[i-1], segments[i]

        i += 1

    return ''.join(segments)
