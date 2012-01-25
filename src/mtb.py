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
import getopt
from mtbxml import Transitions
from mtbhelp import mtb_help

XML_DOC = Transitions()

def main():
    """The Main Procedure"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:s:t:", ["help", "path=", "static=", "transition="])
    except getopt.GetoptError, err:
        print str(err) 
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            mtb_help()
            return
        elif opt in ("-p", "--path"):
            XML_DOC.set_path(arg)
        elif opt in ("-s", "--static"):
            XML_DOC.set_static(arg)
        elif opt in ("-t", "--transition"):
            XML_DOC.set_transition(arg)
        else:
            assert False, "unhandled option"
    XML_DOC.build()

if (__name__=="__main__"):
    main()
