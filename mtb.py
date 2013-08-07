#! /usr/bin/python
""" Yet another, veryt simple background switcher for the Gnome 3 Desktop

 mtb.py
 Copyright (C) Paul Pritchard 2013 
 
 MTB is free software: you can redistribute it and/or modify it under the 
 terms of the GNU General Public License as published by the Free Software 
 Foundation, either version 3 of the License, or (at your option) any 
 later version.
 
 MTB is distributed in the hope that it will be useful, but WITHOUT ANY 
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
 FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program.  If not, see <http://www.gnu.org/licenses/>."""

import os
import random
import mimetypes
from time import localtime, struct_time

time_now = localtime()
hour_now = str(time_now.tm_hour)
if len(hour_now) == 1:
    hour_now = '0' + hour_now

backgrounds = os.environ['HOME'] + "/Pictures/Backgrounds/"
timefolders = os.walk(backgrounds).next()[1]
timefolders.sort()
timefolders.reverse()
current_folder = ''
for tick in timefolders:
    if current_folder == '' and tick >= '00' and tick <= '24': 
        current_folder = tick + '/'
    if tick >= '00' and tick <= '24' and tick <= hour_now:
        current_folder = tick + '/'
        break

backgrounds = backgrounds + current_folder
pictures = []
for filename in os.listdir(backgrounds):
    mimetype = mimetypes.guess_type(filename)[0]
    if mimetype and mimetype.split('/')[0] == "image":
        pictures.append (filename)

picture = random.randrange (0, len(pictures))
fullpath = '"file:///' + backgrounds + pictures[picture] + '"'
os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri '%s'" % (fullpath))
