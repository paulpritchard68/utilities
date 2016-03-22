#! /usr/bin/python
""" Yet another, very simple background switcher for the Gnome 3 Desktop

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
from time import localtime
import subprocess

def current_picture():
    path_now = str(subprocess.check_output(["DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings get org.gnome.desktop.background picture-uri"], shell=True)).split("/")
    picture_now = path_now[len(path_now)-1]
    return picture_now[0:len(picture_now)-2]


def select_picture(backgrounds):
    pictures = []
    for filename in os.listdir(backgrounds):
        mimetype = mimetypes.guess_type(filename)[0]
        if mimetype and mimetype.split('/')[0] == "image":
            pictures.append(filename)
    picture = random.randrange(0, len(pictures))
    current = current_picture()
    if pictures[picture] == current:
        picture = pictures.index(current) + 1
        if picture >= len(pictures):
            picture = 0
    fullpath = '"file:///' + backgrounds + pictures[picture] + '"'
    return fullpath

def switch_wallpaper():

    while 1 == 1:
        time_now = localtime()
        hour_now = str(time_now.tm_hour)
        if len(hour_now) == 1:
            hour_now = '0' + hour_now

        backgrounds = os.environ['HOME'] + "/Pictures/Backgrounds/"
        timefolders = sorted(os.walk(backgrounds), reverse=True)
        current_folder = ''
        for tick in timefolders:
            tock = str(tick[0])[-2:]
            if current_folder == '' and tock >= '00' and tock <= '23':
                current_folder = tock + '/'
            if tock >= '00' and tock <= '23' and tock <= hour_now:
                current_folder = tock + '/'
                break

        backgrounds = backgrounds + current_folder
        fullpath = select_picture(backgrounds)
        os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri '%s'" % (fullpath))

        backgrounds = os.environ['HOME'] + "/Pictures/Backgrounds/lock/"
        if os.path.isdir(backgrounds) == True:
            fullpath = select_picture(backgrounds)
            os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.screensaver picture-uri '%s'" % (fullpath))

        return

switch_wallpaper()
