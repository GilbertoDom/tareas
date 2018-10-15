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


file_list, download_time, instruments =fgetcols("list-of-download-files.dat")
utc_now= datetime.utcnow()
time_str = utc_now.strftime("%Y-%m-%d-%H%-M%-S-")

timestamps = {}
with open("list-of-timestamps.dat") as f:
    for line in f:
       (key, val) = line.split('@@')
       timestamps[key] = str(val)
       #print line

new_timestamps={}
for url, timing, inst in zip(file_list,download_time,instruments):
    download=False

    try:    
        last_timestamp= timestamps[str(url)].rstrip('\n')
        delta_time = timedelta(seconds=int(timing))
        last_time = datetime.strptime(last_timestamp, '%Y/%m/%d %H:%M:%S')
        tick_time = last_time + delta_time
        #print 'Timming last/tick/now '+str(last_time) 
        #+' / '+str(tick_time)+' / ' + str(utc_now)
    except KeyError as keyerror:
        #print 'Error '+str(keyerror)
        download=True
    


    if download or (tick_time < utc_now):        
        file_name = str(inst)
        try:        
            new_file_name = (str(time_str)+str(file_name))    
            response = urllib2.urlopen(url)
            with open(new_file_name, 'w') as f: f.write(response.read())        
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

        
	

