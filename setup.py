# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:14:05 2017

@author: Lysenthia
"""

from distutils.core import setup
import py2exe




setup(windows=[{"script": "2cbz.py",
                "icon_resources": [(1, "gabby.ico")]}],
                options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
                requires=['zipfile','os'],
                excludes=['_ssl',  # Exclude _ssl
                                 'pyreadline', 'difflib', 'doctest', 'locale',
                                 'optparse', 'pickle', 'calendar', 'pbd', 'unittest', 'inspect'],
                zipfile = None)