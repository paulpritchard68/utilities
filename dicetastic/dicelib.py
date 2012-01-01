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
	def __init__(self):
		self.sides = 6
		self.count = 1

	def setSides(self, sides):
		self.sides = sides

	def setCount(self, count):
		self.count = count

	def rollDice(self):
		'Rolls the selected dice'
		self.rolls = []
		for i in range(0, self.count):
			self.rolls.append(random.randrange(self.sides) + 1)
		return self.rolls
