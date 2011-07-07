#!/usr/bin/python
#
# mtb.py
# Copyright (C) Paul Pritchard 2011 <paulpritchard68@gmail.com>
# 
# Macsen's Transitioning Background is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Macsen's Transitioning Background is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import getopt
from mtbxml import Background
from mtbhelp import help

XMLdoc=Background()

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hp:s:t:", ["help", "path=", "static=", "transition="])
	except getopt.GetoptError, err:
		print str(err) 
		sys.exit(2)
	for o, a in opts:
		if o in ("-h", "--help"):
			help()
			return
		elif o in ("-p", "--path"):
			XMLdoc.setPath(a)
		elif o in ("-s", "--static"):
			XMLdoc.setStatic(a)
		elif o in ("-t", "--transition"):
			XMLdoc.setTransition(a)
		else:
			assert False, "unhandled option"
	XMLdoc.build()

if (__name__=="__main__"):
	main()