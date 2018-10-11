#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Perceptron Simple, main script

"""

import perceptron
import pandas as pd
import numpy as np



def build_dataframes(filename):
	df = pd.read_csv(filename)
	msk = np.random.rand(len(df)) < 0.7

	X_train = df[msk]
	Y_train = X_train["class"]
	X_train = X_train.drop(axis=1, columns='class')
	t_w_class = df[~msk]
	X_test = t_w_class.drop(axis=1, columns='class')

	return X_train, Y_train, X_test, t_w_class