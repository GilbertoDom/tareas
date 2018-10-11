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
	np.random.seed(42)
	df = pd.read_csv(filename)
	msk = np.random.rand(len(df)) < 0.7

	X_train = df[msk]
	Y_train = X_train["class"]
	X_train = X_train.drop(axis=1, columns='class')
	t_w_class = df[~msk]
	X_test = t_w_class.drop(axis=1, columns='class')
	test_class = t_w_class.iloc[:,-1]

	return X_train, Y_train, X_test, test_class

def evaluate(predicted, real):
	
	tp = 0
	fn = 0
	tn = 0
	fp = 0

	for y_obtained, dx in zip(predicted, real.values):
		if dx == 1:
			if y_obtained == 1:
				tp += 1
			else:
				fn += 1
		else:
			if y_obtained == -1:
				tn += 1
			else:
				fp += 1

	recall = tp / (tp+fn)
	#y.append(recall)
	false_alarm = fp / (fp+tn)
	#x.append(false_alarm)
	precision = tp / (tp+fp)
	f1score = (2 * (recall*precision))/(recall+precision)
	accuaracy = (tp + tn) / (tp + fp + tn + fn)
	s = "Resultados del clasificador en la validacion :\n\tExactitud: {:0.2f}%\n\tSensibilidad : {:0.2f}%\n\tFalsa Alarma: {:0.2f}%\n\tPrecisión: {:0.2f}%\n\tF1 Score: {:0.2f}\n".format( accuaracy*100, recall*100, false_alarm*100, precision*100, f1score)
	
	print()
	print (s)


if __name__ == '__main__':
	files = ["Iris-setosa", "Iris-virginica", "Iris-versicolor"]

	clf = perceptron.Perceptron(alpha=0.3, epochs=10)
	X_train, y, X_test, real_class = build_dataframes(files[2])
	clf.fit(X_train, y)
	predicted = clf.predict(X_test)
	evaluate(predicted, real_class)