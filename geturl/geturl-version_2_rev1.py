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
# Mar 01, 2017 : geturl version 2.0 
# Mar 01, 2017 : Improves for version 2.0 include implementation of functions to download files, to check if
#                a file has been downloaded and when, and the creation of timestamps with the propouse of 
#                mesuring time for frequency  of download and latest update. 
# Created on Dec 8, 2016

import urllib2
import time
import os, sys
import shutil
import calendar 
from datetime import datetime, timedelta
from readcol import fgetcols
import pytz
from os.path import basename

############-------->CHECK IF SPACES OR TABS<-----------############

import logging

def check_downloaded_file(timestamps, url):
    #last_time = utc_now.strftime("%Y/%m/%d %H:%M:%S")    
    try:    
        last_timestamp= timestamps[str(url)].rstrip('\n')
        #delta_time = timedelta(seconds=int(latest_download))
        last_time =  datetime.utcnow() - datetime.strptime(last_timestamp, '%Y/%m/%d%H:%M:%S')
        #tick_time = last_time + delta_time
        #print 'Timming last/tick/now '+str(last_time) 
        #+' / '+str(tick_time)+' / ' + str(utc_now)
        download=True
    except KeyError as keyerror:
        #print 'Error '+str(keyerror)
        download=False
    return download, last_time

def download_file(url,new_file_name):
    try:        
        response = urllib2.urlopen(url)
        with open(new_file_name, 'w') as f: f.write(response.read())
        flag_error=False
    except Exception as url_error:
        print "URL Error downloading "+str(url)+": "+ str(url_error)
        flag_error=True
    return flag_error

def write_timestamp(timestamps_file,url):
    print timestamps_file
    timestamps = {}
    with open(timestamps_file) as f:
        for line in f:
            (key, val) = line.split('@@')
            timestamps[key] = str(val)
    utc_now= datetime.utcnow()
    timestamps[url]=utc_now.strftime('%Y/%m/%d%H:%M:%S')
    with open(timestamps_file,"w") as f:
        for key, value in timestamps.iteritems():
            f.write(str(key)+'@@'+str(value)+'\n')
    

    


logger = logging.getLogger('geturl')
hdlr = logging.FileHandler('/home/nomada/Documentos/GILX/dev/geturl/geturl.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)


logger.error('Running geturl')

#PATH='/home/lasce/images/'
PATH='/home/nomada/Documentos/GILX/dev/geturl/images/'

#SOURCE_PATH='/home/lasce/Documents/G/dev/geturl/'
SOURCE_PATH='/home/nomada/Documentos/GILX/dev/geturl/'

timestamps_file_store=SOURCE_PATH+"list-of-timestamps-store.dat"
timestamps_file_latest=SOURCE_PATH+"list-of-timestamps-latest.dat"

file_list,latest ,download_freq, instruments =fgetcols(SOURCE_PATH+"list-of-download-files.dat")
utc_now= datetime.utcnow()
time_str = utc_now.strftime("%Y-%m-%d-%H%-M%-S-")

latest_image_dir = PATH
dir_utctime_str = utc_now.strftime("%Y/%m/%d/")

path_dir_name = str(PATH)+str(dir_utctime_str)

if not os.path.exists(latest_image_dir):
    os.makedirs(instrument_dir_name)
       
timestamps = {}
with open(SOURCE_PATH+"list-of-timestamps.dat") as f:
    for line in f:
        (key, val) = line.split('@@')
        timestamps[key] = str(val)

   
for url, latest_download, download_frequency, instrument_file in zip(file_list,latest,download_freq,instruments):

    is_downloaded, delta_time =  check_downloaded_file(timestamps, url)
    directory_name = os.path.splitext(instrument_file)[0]#basename(instrument_file)#instrument_name[:4]
    dir_name = path_dir_name + str(directory_name)+"/"

    
    if not is_downloaded:
        file_name = str(instrument_file)
        new_file_name = (str(dir_name)+str(time_str)+str(file_name))    
        error_flag = download_file(url,new_file_name)
        shutil.copyfile(new_file_name, str(latest_image_dir)+instrument_file)        
        if not error_flag:
            write_timestamp(timestamps_file_latest,url)
            write_timestamp(timestamps_file_store,url)
            logger.error("Downloaded "+str(url))
        else:
            print "Error downloading "+str(url)
            logger.error("Error downloading "+str(url))
    else:
        delta_time_latest = timedelta(seconds=int(latest_download))
        delta_time_store = timedelta(hours=float(download_frequency))
        latest=False
        error_flag=False
        if delta_time >= delta_time_latest:
            error_flag = download_file(url,str(latest_image_dir)+instrument_file)
            if not error_flag:
                write_timestamp(timestamps_file_latest,url)
                logger.error("Downloaded LATEST"+str(url))
                latest=True
            else:
                print "Error downloading LATEST"+str(url)
                logger.error("Error downloading LATEST "+str(url))               
        if delta_time >= delta_time_store:
            if not latest:
                error_flag = download_file(url,new_file_name)
            if not error_flag:
                shutil.copyfile(new_file_name, str(latest_image_dir)+instrument_file)
                write_timestamp(timestamps_file_store,url)
                logger.error("Downloaded STORE"+str(url))
                latest=True
            else:
                print "Error downloading STORE "+str(url)
                logger.error("Error downloading STORE "+str(url))               




#        timestamps = {}
#with open(SOURCE_PATH+"list-of-timestamps.dat") as f:
#    for line in f:
#       (key, val) = line.split('@@')
#       timestamps[key] = str(val)
#       #print line
#       
#new_timestamps={}
#for url, latest_download, download_frequency, instrument_file in zip(file_list,latest,download_freq,instruments):
#    download=False
#
#    directory_name = os.path.splitext(instrument_file)[0]#basename(instrument_file)#instrument_name[:4]
#    dir_name = path_dir_name + str(directory_name)+"/"
#
#    if not os.path.isdir(dir_name):
#        os.makedirs(dir_name)
#        print ("\n"+dir_name + "created")
#    
#    
#    try:    
#        last_timestamp= timestamps[str(url)].rstrip('\n')
#        delta_time = timedelta(seconds=int(latest_download))
#        last_time = datetime.strptime(last_timestamp, '%Y/%m/%d %H:%M:%S')
#        tick_time = last_time + delta_time
#        #print 'Timming last/tick/now '+str(last_time) 
#        #+' / '+str(tick_time)+' / ' + str(utc_now)
#    except KeyError as keyerror:
#        #print 'Error '+str(keyerror)
#        download=True
#        last_time = utc_now.strftime("%Y/%m/%d %H:%M:%S") 
#
#    if download or (tick_time < utc_now):        
#        file_name = str(instrument_file)
#        try:        
#            new_file_name = (str(dir_name)+str(time_str)+str(file_name))    
#            response = urllib2.urlopen(url)
#            with open(new_file_name, 'w') as f: f.write(response.read())
#            shutil.copyfile(new_file_name, str(latest_image_dir)+instrument_file)
#        except Exception as url_error:
#            print "URL Error downloading "+str(url)+": "+ str(url_error)
#            new_timestamps[url]=last_time
#            continue
#        print 'DOWNLOADED File '+str(new_file_name)
#        new_timestamps[url]=utc_now
#
#    else:
#        print 'SKIPED File '+str(url)+str(tick_time)+'  ' + str(utc_now)
#        new_timestamps[url]=last_time
#
#
#        
#with open("list-of-timestamps.dat","w") as f:
#    for key, value in new_timestamps.iteritems():
#        f.write(str(key)+'@@'+value.strftime('%Y/%m/%d %H:%M:%S')+'\n' )
#
