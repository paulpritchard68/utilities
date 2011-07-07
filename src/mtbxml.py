# mtbxml.py
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

import os
import mimetypes
from xml.dom.minidom import Document

class Background:
	def __init__(self):
		self.static=1200
		self.transition=5
		self.path='/usr/share/backgrounds/macsen/'
	def setStatic(self, value):
		self.static=value
	def getStatic(self):
		return self.static
	def setTransition(self, value):
		self.transition=value
	def getTransition(self):
		return self.transition
	def setPath(self, value):
		self.path=value
	def getPath(self):
		return self.path
	def build(self):
		BackgroundXML=Document()

		Background=BackgroundXML.createElement("background")
		BackgroundXML.appendChild(Background)
		
		StartTime=BackgroundXML.createElement("starttime")
		Background.appendChild(StartTime)

		Year=BackgroundXML.createElement("year")
		Year.appendChild(BackgroundXML.createTextNode("2007"))
		StartTime.appendChild(Year)

		Month=BackgroundXML.createElement("month")
		Month.appendChild(BackgroundXML.createTextNode("03"))
		StartTime.appendChild(Month)

		Day=BackgroundXML.createElement("day")
		Day.appendChild(BackgroundXML.createTextNode("21"))
		StartTime.appendChild(Day)

		Hour=BackgroundXML.createElement("hour")
		Hour.appendChild(BackgroundXML.createTextNode("00"))
		StartTime.appendChild(Hour)

		Minute=BackgroundXML.createElement("minute")
		Minute.appendChild(BackgroundXML.createTextNode("00"))
		StartTime.appendChild(Minute)

		Second=BackgroundXML.createElement("second")
		Second.appendChild(BackgroundXML.createTextNode("00"))
		StartTime.appendChild(Second)

		
		ImageList=os.listdir (self.path)
		FirstImage=True
		for image in ImageList:
			mimetype = mimetypes.guess_type (image)[0]
			if mimetype and mimetype.split ('/')[0] == "image":
				if FirstImage==False:
					Transition=BackgroundXML.createElement("transition")
					Background.appendChild(Transition)

					Duration=BackgroundXML.createElement("duration")
					Duration.appendChild(BackgroundXML.createTextNode(str(self.getTransition ())))
					Transition.appendChild(Duration)

					From=BackgroundXML.createElement("from")
					From.appendChild(BackgroundXML.createTextNode(self.getPath () + PreviousImage))
					Transition.appendChild(From)

					To=BackgroundXML.createElement("to")
					To.appendChild(BackgroundXML.createTextNode(self.getPath () + image))
					Transition.appendChild(To)
				
				Static=BackgroundXML.createElement("static")
				Background.appendChild(Static)

				Duration=BackgroundXML.createElement("duration")
				Duration.appendChild(BackgroundXML.createTextNode(str(self.getStatic ())))
				Static.appendChild(Duration)

				File=BackgroundXML.createElement("file")
				File.appendChild(BackgroundXML.createTextNode(self.getPath () + image))
				Static.appendChild(File)

				PreviousImage=image

				if FirstImage==True:
					FirstImage=False
					RolloverImage=image
					
		Transition=BackgroundXML.createElement("transition")
		Background.appendChild(Transition)

		Duration=BackgroundXML.createElement("duration")
		Duration.appendChild(BackgroundXML.createTextNode(str(self.transition)))
		Transition.appendChild(Duration)

		From=BackgroundXML.createElement("from")
		From.appendChild(BackgroundXML.createTextNode(self.getPath () + PreviousImage))
		Transition.appendChild(From)

		To=BackgroundXML.createElement("to")
		To.appendChild(BackgroundXML.createTextNode(self.getPath () + RolloverImage))
		Transition.appendChild(To)

		FilePath=self.getPath () + "macsen.xml"
		file=open(FilePath, 'w')
		BackgroundXML.writexml(file, indent="") #, addindent="  ", newl="\n")
		file.close()
	