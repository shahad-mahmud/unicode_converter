import unittest
import pandas as pd

import unicodeconverter as uc


class TestUnicodeConverter(unittest.TestCase):
    def test_convert_bijoy_to_unicode(self):
        test_file_path = 'unicodeconverter_tests.csv'
        test_df = pd.read_csv(test_file_path)

        bijoy_texts = test_df['bijoy_text'].tolist()
        unicode_texts = test_df['unicode_text'].tolist()

        self.maxDiff = None

        for bijoy, unicode in zip(bijoy_texts, unicode_texts):
            converted = uc.convert_bijoy_to_unicode(bijoy)
            print(unicode.strip())
            print(converted.strip())
            for unicode_word, converted_word in zip(unicode.split(), converted.split()):
                if unicode_word != converted_word:
                    print(unicode_word, converted_word)
                    for c1, c2 in zip(unicode_word, converted_word):
                        if ord(c1) != ord(c2):
                            print(f'{c1} -- {ord(c1)}', f'{c2} -- {ord(c2)}')
            print()
            self.assertEqual(unicode.strip(), converted.strip())


if __name__ == '__main__':
    unittest.main()
