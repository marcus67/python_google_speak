# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'requirements.txt')) as f:
    install_requires = f.read().splitlines()

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'CHANGES.md'), encoding='utf-8') as f:
    changes = f.read()

setup(
    name = "python-google-speak",
    version = "0.2",
    description = "Simple class to create speech files using the Google translate URL",
    author = "Marcus Rickert",
    author_email = "marcus.rickert@web.de",
    url = "https://github.com/marcus67/python_google_speak",
    
    install_requires = install_requires,

    scripts = ["google_speak"],

    packages = [ 'python_google_speak', 'python_google_speak.test' ],
    include_package_data = True,
    
    long_description = long_description + changes,
) 
