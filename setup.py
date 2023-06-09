import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pycon',
    version='1.0.0',
    description='A PNG to ICO converter',
    url='https://github.com/sorzkode/pycon',
    author='Mister Riley',
    author_email='sorzkode@proton.me',
    packages=setuptools.find_packages(),
    install_requires=['Pillow', 'PySimpleGUI', 'tkinter'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
