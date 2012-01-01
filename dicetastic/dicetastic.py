#!/usr/bin/python
#
# dicetastic.py
# Copyright (C) Paul Pritchard 2011 <paulpritchard68@gmail.com>
# 
# Dicetastic is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Dicetastic is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from dicelib import Dice 

def RollDice():
	'Prompts for number and type of dice, then rolls them'
	RollThis = Dice()

	d = 0
	while d < 1: 
		numberDtype = raw_input("Ladies and gentlemen, roll the dice: ")

		#Check that the form is [number]d[type]
		d=numberDtype.lower().find("d")
		if d  < 1:
			print "Badly formatted dice string. Try again."
	
	RollThis.setCount(int(numberDtype[0:d]))
	RollThis.setSides(int(numberDtype[d + 1]))

	print RollThis.rollDice()

if __name__ == "__main__":
	RollDice()
