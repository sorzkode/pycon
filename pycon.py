#!/usr/bin/env python3
#%%
'''
██████  ██    ██  ██████  ██████  ███    ██ 
██   ██  ██  ██  ██      ██    ██ ████   ██ 
██████    ████   ██      ██    ██ ██ ██  ██ 
██         ██    ██      ██    ██ ██  ██ ██ 
██         ██     ██████  ██████  ██   ████ 
                                            
                                                                                                                                                                                                                                                                                                                
A PNG to ICO image converter made with PySimpleGUI and Pillow.
-
Author:
Mister Riley
sorzkode@proton.me
https://github.com/sorzkode

MIT License
Copyright (c) 2023 Mister Riley
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Dependencies
from tkinter.font import BOLD, ITALIC
import PySimpleGUI as sg
from PIL import Image
from os.path import exists

# Font styles
FONT_TITLE = ('Lucida', 14, BOLD)
FONT_SUBTITLE = ('Lucida', 12, ITALIC)
FONT_BUTTON = ('Lucida', 12, BOLD)
FONT_SUBTEXT = ('Lucida', 10, BOLD)

# PySimpleGUI version info
SGVERSION = sg.version

# GUI window theme
sg.theme("Default1")

# Application dropdown menu
APP_MENU = [["&Help", ["&Usage", "&About"]]]

# All GUI elements
LAYOUT = [
    [
        sg.Menu(
            APP_MENU,
            tearoff=False,
            key='-MENU-'
            )
    ],
    [
        sg.Image(
            filename='assets\pyclogo.png',
            key='-LOGO-'
            )
    ],
    [
        sg.Text(
            "Image Selection:",
            font=FONT_TITLE
            ),
        sg.In(
            "Select your PNG file...",
            font=FONT_SUBTITLE,
            pad=(5, 15),
            enable_events=True,
            disabled=True,
            key='-FILEPATH-'
            ),
        sg.Button(
            "Browse",
            font=FONT_BUTTON,
            pad=(5, 15),
            disabled=False
            ),
    ],
    [
        sg.Text(
            "ICO Properties:",
            font=FONT_SUBTEXT
            ),
        sg.Spin(
            values=(
                "16x16",
                "24x24",
                "32x32",
                "64x64",
            ),
            initial_value=
                "32x32",
            disabled=True,
            enable_events=True,
            readonly=True,
            key='-PROPERTIES-'
            ),
    ],
    [
        sg.Button(
            "Convert",
            font=FONT_BUTTON,
            pad=(5, 15),
            disabled=True
            ),
        sg.Button(
            "Clear",
            font=FONT_BUTTON,
            pad=(5, 15),
            disabled=True
            ),
        sg.Button(
            "Exit", 
            font=FONT_BUTTON,
            pad=(5, 15)
            ),
    ],
]

class PyconWindow:

    '''Initializing main application'''

    def __init__(self, window):
        self.window = sg.Window(
            "Pycon",
            LAYOUT,
            resizable=True,
            icon="assets\pycon.ico",
            grab_anywhere=True,
            keep_on_top=True,
        )
        self.start()

    def image_selection(self):

        '''Selecting PNG Image to convert to ICO'''

        png_image = sg.popup_get_file(
            'Select a PNG Image for conversion',
            file_types=(("Image Files",
                "*.png"),),
                title='File Selection',
                grab_anywhere=True,
                keep_on_top=True
                )
      
        if not png_image:
            sg.popup_cancel(
                'No file selected, try again',
                grab_anywhere=True,
                keep_on_top=True
                )
            return None

        self.window['-PROPERTIES-'].update(disabled=False)
        self.window['Convert'].update(disabled=False)
        self.window['-FILEPATH-'].update(png_image)
        return png_image

    def reset_defaults(self):

        '''Application interface defaults'''

        self.window['-FILEPATH-'].update("Cleared....select a new PNG file")
        self.window['-PROPERTIES-'].update(disabled=True)
        self.window['Convert'].update(disabled=True)

    def save_location(self):

        '''Defining save path for new ICO file'''

        save_path = sg.popup_get_folder(
            'Select Save Location',
            title='Folder Selection',
            grab_anywhere=True,
            keep_on_top=True
            )
        
        if not save_path:
            sg.popup_cancel(
                'No folder selected, try again',
                grab_anywhere=True,
                keep_on_top=True
                )
            return None
        return save_path

    def new_name(self):

        '''Defining ICO file name'''

        ico_name = sg.popup_get_text(
            'Enter a name for your ICO file',
            title='ICO Name',
            grab_anywhere=True,
            keep_on_top=True
            )
        
        if not ico_name:
            sg.popup_cancel(
                'No name entered, try again',
                grab_anywhere=True,
                keep_on_top=True
                )
            return None
        return ico_name
   
    def convert_image(self):
        png_image = self.values['-FILEPATH-']
        save_path = self.save_location()
        ico_name = self.new_name()
        ico_properties = self.values['-PROPERTIES-']

        size_mapping = {
            '16x16': (16, 16),
            '24x24': (24, 24),
            '32x32': (32, 32),
            '64x64': (64, 64)
        }

        ico_width, ico_height = size_mapping.get(ico_properties, (32, 32))

        new_file = str(save_path + '/' + ico_name + '.ico')
        file_exists = exists(new_file)

        open_image = Image.open(png_image)

        if file_exists:
            warning_message = sg.popup_ok_cancel(
                f"WARNING! {ico_name} already exists in this directory. Replace?",
                grab_anywhere=True,
                keep_on_top=True
            )
            if warning_message == "OK":
                try:
                    open_image.save(
                        new_file,
                        format='ICO',
                        sizes=[(ico_width, ico_height)]
                    )
                    sg.popup(
                        'Success!',
                        grab_anywhere=True,
                        keep_on_top=True,
                    )
                    self.reset_defaults()
                except Exception as e:
                    sg.popup(
                        f'Error while saving the ICO file: {str(e)}',
                        grab_anywhere=True,
                        keep_on_top=True,
                    )
            else:  # Cancel button was clicked
                sg.popup(
                    'Conversion cancelled. Try another name.',
                    grab_anywhere=True,
                    keep_on_top=True
                )
        else:
            try:
                open_image.save(
                    new_file,
                    format='ICO',
                    sizes=[(ico_width, ico_height)]
                )
                sg.popup(
                    'Success!',
                    grab_anywhere=True,
                    keep_on_top=True,
                )
                self.reset_defaults()
            except Exception as e:
                sg.popup(
                    f'Error while saving the ICO file: {str(e)}',
                    grab_anywhere=True,
                    keep_on_top=True,
                )


    def about_gui(self):

        '''About menu item'''

        sg.popup(
            "A PNG to ICO converter.",
            "",
            "Author: Mister Riley",
            "Website: https://github.com/sorzkode",
            "License: MIT",
            "",
            f"PySimpleGUI Version: {SGVERSION}",
            "",
            grab_anywhere=True,
            keep_on_top=True,
            title="About",
        )

    def usage_gui(self):

        '''Usage menu option'''

        sg.popup(
            "Follow these basic steps:",
            "",
            '1. Click the "Browse" button to select your PNG file',
            '2. Use the spinbox to set your ICO dimensions',
            '3. Click the "Convert" button',
            '4. Select your save path',
            '5. Type a name for your ICO file',
            "",
            grab_anywhere=True,
            keep_on_top=True,
            title="Usage",
        )

    def start(self):

        '''Initilization function'''

        # Event loops when buttons are pressed / actions are taken in the app
        while True:
            self.event, self.values = self.window.read()

            # Window closed event
            if self.event == sg.WIN_CLOSED or self.event == "Exit":
                break
            # Matching events to functions
            match self.event:
                case "Browse":
                    self.image_selection()
                case "Convert":
                    self.convert_image()
                case "Clear":
                    self.reset_defaults()
                case "About":
                    self.about_gui()
                case "Usage":
                    self.usage_gui()

        self.window.close()

if __name__ == "__main__":
    PyconWindow(sg)
# %%
