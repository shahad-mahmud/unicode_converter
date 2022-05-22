# Unicode Converter

[![python versions](https://img.shields.io/pypi/pyversions/unicodeconverter)](https://img.shields.io/pypi/pyversions/unicodeconverter) [![pypi version](https://img.shields.io/pypi/v/unicodeconverter)](https://img.shields.io/pypi/v/unicodeconverter) [![pypi downloads](https://pepy.tech/badge/unicodeconverter)](https://pepy.tech/project/unicodeconverter)
A python tool to convert Bangla Bijoy text to Unicode text.

## Installation

Unicode Converter can be installed via PyPi. Make sure `pip` is installed and updated. Then simply run the following command:

```bash
pip install unicodeconverter
```

## How to use

```python
import unicodeconverter as uc

bijoy_text = 'Avwg evsjvq Mvb MvB|'
unicode_text = uc.convert_bijoy_to_unicode(bijoy_text)

print(unicode_text)
# >>> আমি বাংলায় গান গাই।
```
