#!/usr/bin/python
"""An XML based background switcher for the Gnome Desktop

setup.py
 The standard build script
 Copyright (C) Paul Pritchard 2011 <paulpritchard68@gmail.com>
 
 Macsen's Transitioning Background is free software: you can redistribute it 
 and/or modify it under the terms of the GNU General Public License as 
 published by the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 Macsen's Transitioning Background is distributed in the hope that it will be 
 useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
 See the GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program.  If not, see <http://www.gnu.org/licenses/>."""

from distutils.core import setup

setup(
    name = "mtb",
    version = '0.2',
    description = "Macsen's Transitioning Background",
    long_description = ('An XML based background switcher for Gnome 2'),
    author = 'Paul Pritchard',
    author_email = 'paulpritchard68@gmail.com',
    url = 'http://www.expatpaul.eu/mtb/', 

    license="GPLv3+",
    
    data_files = (['README']),
    py_modules = ['src/mtb', 'src/mtbxml'],

    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python'
        ]

    )
