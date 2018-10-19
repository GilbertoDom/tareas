#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Perceptron Simple, One vs All classification

"""

import perceptron as p
import numpy as np


def OneVsAll(params,df):
    alpha, epochs = 0.1, 10
    perceps = {}
    predicted = []
    for name, t in params.items():
        w, theta = t[0], t[1]
        O = p.Perceptron(alpha, epochs)
        O.w = w
        O.theta = theta
        perceps[name] = O

    setosa = perceps['Iris-setosa']
    virginica = perceps['Iris-virginica']
    versi = perceps['Iris-versicolor']
	
    for instance in df.values:	
        #setosa_net = np.fabs(setosa.net_input(instance, setosa.w, setosa.theta))
        #virginica_net = np.fabs(virginica.net_input(instance, virginica.w, virginica.theta))
        #versi_net = np.fabs(versi.net_input(instance, versi.w, versi.theta))
        setosa_net = setosa.net_input(instance, setosa.w, setosa.theta)
        virginica_net = virginica.net_input(instance, virginica.w, virginica.theta)
        versi_net = versi.net_input(instance, versi.w, versi.theta)
        
        nets = [setosa_net, virginica_net, versi_net]
        highest = max(nets)
        
        if highest == setosa_net:
            clase = 'Iris-setosa'
        elif highest == virginica_net:
            clase = 'Iris-virginica'
        else:
            clase = 'Iris-versicolor'
        predicted.append(clase)

    #print(predicted)

    return predicted

def evaluate_ova(predicted, real_y):

	correctos = 0
	for y_obtenida, y_real in zip(predicted, real_y.values):
		if y_obtenida == y_real:
			correctos += 1
	
	exactitud = correctos/len(real_y)
	print('Accuaracy of OvA prediction: {:0.2f}%'.format(exactitud*100))


#if __name__ == '__main__':

#	alpha = 0.2773
#	epochs = 20






