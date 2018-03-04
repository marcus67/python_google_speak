# -*- coding: utf-8 -*-

import os
from setuptools import setup

setup(
    name = "python-google-speak",
    version = "0.1",
    description = "Simple class to create speech files using Google translate URL",
    author = "Marcus Rickert",
    author_email = "marcus.rickert@web.de",
    url = "TODO",
    
    install_requires=['requests', 'playsound'],
    
    packages = [ 'python_google_speak' ],
    include_package_data = True,
    
    long_description = """TODO""",
) 
