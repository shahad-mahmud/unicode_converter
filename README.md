# Unicode Converter
A python tool to convert Bangla Bijoy text to Unicode text. 

# Installation
Unicode Converter can be installed via PyPi. Make sure `pip` is installed and updated. Then simply run the following command:
    
    pip install unicodeconverter


# how to use
    import unicodeconverter as uc

    bijoy_text = 'Avwg evsjvq Mvb MvB|'
    unicode_text = uc.convert_bijoy_to_unicode(bijoy_text)

    print(unicode_text)
    # >>> আমি বাংলায় গান গাই। 