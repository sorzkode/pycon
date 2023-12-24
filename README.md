[![CodeQL](https://github.com/sorzkode/pycon/actions/workflows/codeql.yml/badge.svg)](https://github.com/sorzkode/pycon/actions/workflows/codeql.yml)
[![MIT Licence](https://en.wikipedia.org/wiki/MIT_License)]

![PYCON](https://raw.githubusercontent.com/sorzkode/pycon/master/assets/pycgit.png)

# PYCON

PYCON is a PNG to ICO converter made with PySimpleGUI and Pillow.

## Example

![Example](https://raw.githubusercontent.com/sorzkode/pycon/master/assets/example.png)

## Installation

To install PYCON, follow these steps:

1. Download the ZIP from the [GitHub repository](https://github.com/sorzkode/pycon).
2. Extract the ZIP file to a directory of your choice.
3. Open a terminal or command prompt and navigate to the extracted directory.
4. Run the following command to install the dependencies:

    ```
    pip install -r requirements.txt
    ```

    This will install Python 3, PySimpleGUI, Pillow, and tkinter (for Linux users).

5. Once the dependencies are installed, you can run the script using the following command:

    ```
    python pycon.py
    ```

    Alternatively, you can use the following command if you have installed PYCON as a package:

    ```
    python -m pycon
    ```

Note: Installation is not required to run the script, but you need to ensure that the above requirements are met.
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
