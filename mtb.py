#! /usr/bin/python2
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
from time import localtime, struct_time, sleep
import sys
import argparse
from ConfigParser import ConfigParser

def switch_wallpaper():

    while 1 == 1:
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
            if current_folder == '' and tick >= '00' and tick <= '23': 
                current_folder = tick + '/'
            if tick >= '00' and tick <= '23' and tick <= hour_now:
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

        config = ConfigParser()
        config.read(['mtb.cfg', os.path.expanduser('~/.mtb.cfg')])

        try:
            wait_minutes = config.get('Main', 'wait')
            wait_seconds = int(wait_minutes) * 60
        except:
            wait_seconds = 1200

        sleep(wait_seconds)

def set_wait(wait):
    config = ConfigParser()
    config.read(['mtb.cfg', os.path.expanduser('~/.mtb.cfg')])
    config_out = open(os.path.expanduser('~/.mtb.cfg'), 'w')

    try:
        config.set('Main', 'wait', wait)
    except:
        config.add_section('Main')
        config.set('Main', 'wait', wait)
    
    config.write(config_out)
    config_out.close()

def main():
    """ The main event 
        Parses the entered arguments and figures out what to do with them """
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wait', action='store', help='Wait time (minutes)')
    
    try:
        args = parser.parse_args()
    except:
        sys.exit(2)

    if args.wait:
        set_wait(args.wait)
    else:
        switch_wallpaper()

if __name__ == "__main__":
    main()
