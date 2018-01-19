#!/usr/bin/python
""" 
A simple file renaming application for removing annoying characters

Copyright (C) 2014 - Paul Pritchard

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>."""

import sys
import os
import mimetypes
import re

def new_name(text_string):
    new_text = re.sub(' ', '_', text_string)
    new_text = re.sub('[()\[\],\'&!?’]', '', new_text)
    new_text = re.sub('_-_', '-', new_text)
    new_text = re.sub('__', '_', new_text)
    new_text = re.sub('\.{3}', '', new_text)
    new_text = re.sub('\._', '_', new_text)
    new_text = re.sub('"', '', new_text)
    new_text = re.sub('_–_', '-', new_text)
    new_text = re.sub('–', '', new_text)
    new_text = re.sub('—', '-', new_text)
    return new_text
    
def rename_files():
    """ Iterates through the list of files in the current directory.
        For all  files, attempts to rename the file by replacing the annoying characters """    
    current_path = os.getcwd()
    for dirname, dirnames, filenames in os.walk(current_path):
        new_dir = new_name(dirname)
        os.rename(dirname, new_dir)
        os.chdir(new_dir)
        for filename in filenames:
            mimetype = mimetypes.guess_type(filename)[0]
            os.rename(filename, new_name(filename))

if __name__ == "__main__":
    rename_files()
