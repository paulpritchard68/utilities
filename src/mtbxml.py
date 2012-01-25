# mtbxml.py

""" XML Library for Macsens element_transitioning Background

Copyright (C) 2011 - Paul Pritchard

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

import os
import mimetypes
from xml.dom.minidom import Document

class Transitions:
    """ The document XML Class"""
    
    def __init__(self):
        """ Initialise """
        self.static = 1200
        self.transition = 5
        self.path = '/usr/share/backgrounds/macsen/'
    
    def set_static(self, value):
        """ Sets static time - how lomg each image should be displayed"""
        self.static = value
    
    def get_static(self):
        """ Retrieve static time """
        return self.static
    
    def set_transition(self, value):
        """ Sets transition time """
        self.transition = value
    
    def get_transition(self):
        """ Retrieve transition time """
        return self.transition
    
    def set_path(self, value):
        """ Sets folder path for the XML """
        self.path = value
    
    def get_path(self):
        """ Retrieves folder path for the XML """
        return self.path
    
    def build(self):
        """ Build the XML file """
        background_xml = Document()

        document = background_xml.createElement("background")
        background_xml.appendChild(document)
        
        start_time = background_xml.createElement("starttime")
        document.appendChild(start_time)

        start_year = background_xml.createElement("year")
        start_year.appendChild(background_xml.createTextNode("2007"))
        start_time.appendChild(start_year)

        start_month = background_xml.createElement("month")
        start_month.appendChild(background_xml.createTextNode("03"))
        start_time.appendChild(start_month)

        start_day = background_xml.createElement("day")
        start_day.appendChild(background_xml.createTextNode("21"))
        start_time.appendChild(start_day)

        start_hour = background_xml.createElement("hour")
        start_hour.appendChild(background_xml.createTextNode("00"))
        start_time.appendChild(start_hour)

        start_minute = background_xml.createElement("minute")
        start_minute.appendChild(background_xml.createTextNode("00"))
        start_time.appendChild(start_minute)

        start_second = background_xml.createElement("second")
        start_second.appendChild(background_xml.createTextNode("00"))
        start_time.appendChild(start_second)

        
        image_list = os.listdir (self.path)
        first_image = True
        for image in image_list:
            mimetype = mimetypes.guess_type (image)[0]
            if mimetype and mimetype.split ('/')[0] == "image":
                if first_image == False:
                    element_transition = background_xml.createElement("transition")
                    document.appendChild(element_transition)

                    element_duration = background_xml.createElement("duration")
                    element_duration.appendChild(background_xml.createTextNode(str(self.get_transition ())))
                    element_transition.appendChild(element_duration)

                    element_from = background_xml.createElement("from")
                    element_from.appendChild(background_xml.createTextNode(self.get_path () + previous_image))
                    element_transition.appendChild(element_from)

                    element_to = background_xml.createElement("to")
                    element_to.appendChild(background_xml.createTextNode(self.get_path () + image))
                    element_transition.appendChild(element_to)
                
                element__static = background_xml.createElement("static")
                document.appendChild(element__static)

                element_duration = background_xml.createElement("duration")
                element_duration.appendChild(background_xml.createTextNode(str(self.get_static ())))
                element__static.appendChild(element_duration)

                element_file = background_xml.createElement("file")
                element_file.appendChild(background_xml.createTextNode(self.get_path () + image))
                element__static.appendChild(element_file)

                previous_image = image

                if first_image == True:
                    first_image = False
                    rollover_image = image
                    
        element_transition = background_xml.createElement("transition")
        document.appendChild(element_transition)

        element_duration = background_xml.createElement("duration")
        element_duration.appendChild(background_xml.createTextNode(str(self.transition)))
        element_transition.appendChild(element_duration)

        element_from = background_xml.createElement("from")
        element_from.appendChild(background_xml.createTextNode(self.get_path () + previous_image))
        element_transition.appendChild(element_from)

        element_to = background_xml.createElement("to")
        element_to.appendChild(background_xml.createTextNode(self.get_path () + rollover_image))
        element_transition.appendChild(element_to)

        file_path = self.get_path () + "macsen.xml"
        file_name = open(file_path, 'w')
        background_xml.writexml(file_name, indent="") #, addindent="  ", newl="\n")
        file_name.close()
    
