#!/usr/bin/python
"""An XML based background switcher for the Gnome Desktop

 mtb.py
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

import sys
import argparse
from mtbxml import Transitions
from mtbhelp import mtb_help

XML_DOC = Transitions()

def main():
    """ The Main Procedure
        Parses the options and executes the build function"""

    parser = argparse.ArgumentParser(description='Create a transitioning background XML for Gnome 2')
    parser.add_argument('-p', '--path', action='store', help='Set path for images and XML')
    parser.add_argument('-s', '--static', action='store', help='Set static time in seconds')
    parser.add_argument('-t', '--transition', action='store', help='Set transiton time in seconds')

    try:
        options = parser.parse_args()
    except:
        sys.exit(2)

    if options.path is not None:
        XML_DOC.set_path(options.path)
    if options.static is not None:
        XML_DOC.set_static(options.static)
    if options.transition is not None:
        XML_DOC.set_transition(options.transition)
    
    XML_DOC.build()

if (__name__=="__main__"):
    main()
