#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Perceptron Simple, preprocesamiento

"""

import pandas as pd 
import numpy as np
"""
¡¡¡ESTANDARIZA LOS DATOS!!!

"""

def data_disctimination_for_perceptron(filename):

	columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid', 'class']
	df = pd.read_csv(filename, names=columns)
	clasv = df.iloc[:,-1]
	clas_vals = np.unique(clasv.values)

	discriminated_classes = {}
	for val in clas_vals:
		L = []
		for cl in clasv.values:
			if cl == val:
				L.append(1)
			else:
				L.append(-1)
		dfs[val] = L


	for dfname, dfm in dfs.items():
		ndf = pd.DataFrame(dfm)
		dfs[dfname] = ndf

	X = df.iloc[:,:-1]

	return discriminated_classes, X 

filename = 'iris.data.txt'

classes_dataframes, data_body = data_disctimination_for_perceptron(filename)

for class_name, df in classes_dataframes.items():
	body = data_body
	D = body.insert(column='class', loc=len(df.keys()), value=df)
	pd.to_csv('.' ,D)






