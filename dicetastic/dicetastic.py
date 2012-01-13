#!/usr/bin/python
"""A command line front end for the dicelib library"""

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

def roll_dice():
    """Prompts for number and type of dice, then rolls them"""
    roll_this = Dice()

    index_d = 0
    while index_d < 1: 
        count_sides = raw_input("Ladies and gentlemen, roll the dice: ")

        #Check that the form is [number]d[type]
        index_d = count_sides.lower().find("d")
        if index_d  < 1:
            print "Badly formatted dice string. Try again."
    
    roll_this.set_count(int(count_sides[0:index_d]))
    roll_this.set_sides(int(count_sides[index_d + 1]))

    print roll_this.roll_dice()

if __name__ == "__main__":
    roll_dice()
