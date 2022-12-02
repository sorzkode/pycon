import setuptools

setuptools.setup(
    name='pycon',
    version='1.0.0',
    description='A PNG to ICO converter.',
    url='https://github.com/sorzkode/',
    author='sorzkode',
    author_email='<sorzkode@proton.me>',
    packages=setuptools.find_packages(),
    install_requires=['Pillow', 'PySimpleGUI', 'tkinter'],
    long_description='A PNG to ICO converter using PySimpleGUI and Pillow.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT',
        'Operating System :: OS Independent',
        ],
)