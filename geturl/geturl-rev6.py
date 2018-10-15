#!/usr/bin/env python
#-*- coding: utf-8 -*-
#    geturl.py Download files from web.
#    Copyright (C) 2017  Gilberto D.(n0m4d) @ lasce
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# HISTORY
# Jan 25, 2017 : Improve for multiple figures.
# Jan 27, 2017 : Improve for easy download-file input.
# Jan 31, 2017 : Improve for saving files using PATH dirs.
# Feb 08, 2017 : Improve for saving files on utc-time named dirs and latest image downloaded.
# Feb 15, 2017 : Improved for logging file.
# Created on Dec 8, 2016

import urllib2
import time
import os, sys
import shutil
import calendar 
from datetime import datetime, timedelta
from readcol import fgetcols
import pytz

############-------->CHECK IF SPACES OR TABS<-----------############

import logging

logger = logging.getLogger('geturl')
hdlr = logging.FileHandler('/home/lasce/Documents/G/dev/geturl/geturl.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)


logger.error('Running geturl')

PATH='/home/lasce/images/'
SOURCE_PATH='/home/lasce/Documents/G/dev/geturl/'

file_list,latest ,download_freq, instruments =fgetcols(SOURCE_PATH+"list-of-download-files.dat")
utc_now= datetime.utcnow()
time_str = utc_now.strftime("%Y-%m-%d-%H%-M%-S-")

instrument_dir_name = PATH#+"/instrument-latest/"
dir_utctime_str = utc_now.strftime("%Y/%m/%d/")

dir_name = str(PATH)+str(dir_utctime_str)

#if not os.path.exists(dir_name):
#    os.makedirs(dir_name)
if not os.path.exists(instrument_dir_name):
    os.makedirs(instrument_dir_name)

timestamps = {}
with open(SOURCE_PATH+"list-of-timestamps.dat") as f:
    for line in f:
       (key, val) = line.split('@@')
       timestamps[key] = str(val)
       #print line

new_timestamps={}
for url, latest_download, download_frequency, instrument_name in zip(file_list,latest,download_freq,instruments):
    download=False

    if  instrument_name.endswith(".jpg"):
        directory_name = instrument_name[:-4]
    else:
        directory_name = instrument_name[:-4]
    
    dir_name = dir_name + str(directory_name)+"/"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    
    try:    
        last_timestamp= timestamps[str(url)].rstrip('\n')
        delta_time = timedelta(seconds=int(latest_download))
        last_time = datetime.strptime(last_timestamp, '%Y/%m/%d %H:%M:%S')
        tick_time = last_time + delta_time
        #print 'Timming last/tick/now '+str(last_time) 
        #+' / '+str(tick_time)+' / ' + str(utc_now)
    except KeyError as keyerror:
        #print 'Error '+str(keyerror)
        download=True
        last_time = utc_now.strftime("%Y/%m/%d %H:%M:%S") 

    if download or (tick_time < utc_now):        
        file_name = str(instrument_name)
        try:        
            new_file_name = (str(dir_name)+str(time_str)+str(file_name))    
            response = urllib2.urlopen(url)
            with open(new_file_name, 'w') as f: f.write(response.read())
            shutil.copyfile(new_file_name, str(instrument_dir_name)+instrument_name)
        except Exception as url_error:
            print "URL Error downloading "+str(url)+": "+ str(url_error)
            new_timestamps[url]=last_time
            continue
        print 'DOWNLOADED File '+str(new_file_name)
        new_timestamps[url]=utc_now

    else:
        print 'SKIPED File '+str(url)+str(tick_time)+'  ' + str(utc_now)
        new_timestamps[url]=last_time


        
with open("list-of-timestamps.dat","w") as f:
    for key, value in new_timestamps.iteritems():
        f.write(str(key)+'@@'+value.strftime('%Y/%m/%d %H:%M:%S')+'\n' )

        
	

