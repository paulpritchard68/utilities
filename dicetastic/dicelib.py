#! /usr/bin/python
""" A dice rolling library """

# dicelib.py
#
# Copyright (C) 2011 - Paul Pritchard
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import random

class Dice:
    """The Dice class. This handles dice set definition and rolling"""
    
    def __init__(self):
        """Initialise the dice with default values of 1d6. 
	No rolls yet, so that's an empty list"""
        self.sides = 6
        self.count = 1
        self.rolls = []

    def set_sides(self, sides):
        """Set the number of sides"""
        self.sides = sides

    def set_count(self, count):
        """Set the number of dice"""
        self.count = count

    def roll_dice(self):
        """Rolls the selected dice"""
        for i in range(0, self.count):
            self.rolls.append(random.randrange(self.sides) + 1)
        return self.rolls
