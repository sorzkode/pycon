[![CodeQL](https://github.com/sorzkode/pycon/actions/workflows/codeql.yml/badge.svg)](https://github.com/sorzkode/pycon/actions/workflows/codeql.yml)
[![MIT Licence](https://en.wikipedia.org/wiki/MIT_License)]

![PYCON](https://raw.githubusercontent.com/sorzkode/pycon/master/assets/pycgit.png)

# PYCON

PYCON is a PNG to ICO converter made with PySimpleGUI and Pillow.

## Example

![Example](https://raw.githubusercontent.com/sorzkode/pycon/master/assets/example.png)

## Installation

Download the ZIP from the GitHub repository, change the directory (cd) to the script directory, and run the following command:
```
pip install -e .
```
*This will install the PYCON package locally.

Note: Installation isn't required to run the script, but you need to ensure that the following requirements are met.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
- [Pillow](https://pypi.org/project/Pillow/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (Linux Users)

## Usage

If installed, you can use the following command syntax:
```
python -m pycon
```
Otherwise, you can run the script directly by changing the directory (cd) in a terminal of your choice to the pycon directory and using the following syntax:
```
python pycon.py
```

Once initiated, use the following steps:
```            
1. Click the "Browse" button to select your PNG file.
2. Use the spinbox to set your ICO dimensions.
3. Click the "Convert" button.
4. Select your save path.
5. Type a name for your ICO file.
```
