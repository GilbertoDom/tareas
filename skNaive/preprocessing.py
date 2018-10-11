#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Minería de Datos 
Gilberto Carlos Dominguez Aguilar
Minería de datos con SK-Learn's Naive Bayes: script for preprocessing data

"""

import pandas as pd

#PATH = "/home/nomada/Documentos/progra/Mineria de Datos/"
filename = "SMSSpamCollection"


df = pd.read_csv(filename, sep='\t', names=['class', 'message'])


clase = df["class"]
body = df["message"]



