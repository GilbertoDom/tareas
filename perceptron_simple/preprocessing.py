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


def data_disctimination_for_perceptron(filename):

	columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid', 'class']
	df = pd.read_csv(filename, names=columns)
	clasv = df.iloc[:,-1]
	clas_vals = np.unique(clasv.values)

	discriminated_classes = {}
	dfs = {}
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
		discriminated_classes[dfname] = ndf

	X = df.iloc[:,:-1]
	X = estandarizar_datos(X)
	return discriminated_classes, X 


def estandarizar_datos(df):
	
	dflist = []
	for i in range(df.shape[1]):
		column = df.iloc[:, i]
		promedio = column.mean()
		desviacion = column.std()
		L = []
		for dato in column:
			z = (dato - promedio) / desviacion # estandarizacion no normalizacion
			L.append(z)
		dflist.append(L)
	ndf = pd.DataFrame(dflist)
	ndf = ndf.transpose()
	ndf.columns = ["sep_len", "sep_wid", "pet_len", "pet_wid"]

	return ndf





filename = 'iris.data.txt'

classes_dataframes, data_body = data_disctimination_for_perceptron(filename)

"""
for class_name, df in classes_dataframes.items():
	body = data_body
	body.insert(column='class', loc=len(body.keys()), value=df)
	body.to_csv(class_name, index=False )
	data_body = data_body.drop(axis=1, columns="class")
"""

#EOF



