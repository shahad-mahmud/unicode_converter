from setuptools import setup, find_packages

VERSION = '0.1.0b1'

with open("readme.md") as f:
    long_description = f.read()

setup(
    name='unicodeconverter',
    version=VERSION,
    description='Convert Bangla text from Bijoy to Unicode',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Md. Shahad Mahmud Chowdhury',
    author_email='shahad9381@gmail.com',
    package_dir={'':'unicodeconverter'},
    packages=find_packages('unicodeconverter'),
    url='https://github.com/shahad-mahmud/unicode_converter',
    keywords=['bangla unicode converter', 'bijoy to unicode'],
    python_requires='>=3.3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
