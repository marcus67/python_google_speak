# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

from setuptools import setup

setup(
    name = "python-google-speak",
    version = "0.1",
    description = "Simple class to create speech files using Google translate URL",
    author = "Marcus Rickert",
    author_email = "marcus.rickert@web.de",
    url = "https://github.com/marcus67/python_google_speak",
    
    install_requires=['requests', 'playsound', 'pygi'],

    scripts = ["google_speak"],

    packages = [ 'python_google_speak' ],
    include_package_data = True,
    
    long_description = """Simple class to create speech files using Google translate URL""",
) 
