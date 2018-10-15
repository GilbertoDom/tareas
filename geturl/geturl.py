#-*- coding: utf-8 -*-
import urllib
import time
import os, sys
import shutil
import calendar 


lista = ['http://services.swpc.noaa.gov/images/goes-xray-flux.gif','http://services.swpc.noaa.gov/images/goes-xray-flux-6-hour.gif']


nombreDelArchivo = lista[0].split('/')[-1]
nombreDelArchivo1 = lista[1].split('/')[-1]

#urllib.urlretrieve(urlQueQuiero,nombreDelArchivo)

#urlretrieve tiene hasta cuatro parametros pero solo necesitamos dos,
#lo que va a hacer es obtener el archivo de la url y guardarlo con el
#nombre deseado especificado en el segundo parámetro

urllib.urlretrieve(lista[0],nombreDelArchivo)
urllib.urlretrieve(lista[1],nombreDelArchivo1)

#EL TIEMPO ES TIEMPO LOCAL NO UTC!!!!

timestr = time.strftime("%Y-%m-%d-%H%-M%-S-")
print timestr

nombreDelArchivo = (str(timestr)+str(nombreDelArchivo))    
nombreDelArchivo1 = (str(timestr)+str(nombreDelArchivo1))

print nombreDelArchivo 
print nombreDelArchivo1 

#las impresiones anteriores son solo con fines demostrativos de la estampilla de 
#tiempo y el formato de los nombres del archivo, pueden ser comentadas para que no
#aparezcan 


#el usuario debe revisar que no cambie la estructura de la URL, de ser asi
# la lista que las contiene debe ser modificada
os.rename('goes-xray-flux-6-hour.gif', str(nombreDelArchivo))
os.rename('goes-xray-flux.gif', str(nombreDelArchivo1))


#developed by Gilberto D.(n0m4d) @ lasce
#dec 8 2016
