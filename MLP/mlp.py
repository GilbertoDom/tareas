#! /usr/bin/env python3
#-*- coding:utf-8 -*-

"""
	LTIC, ENES Morelia, UNAM 
	Redes Neuronales Artificiales 
	Multi-Layer Perceptron (MLP), 
	Alejandro Ortiz Ledezma, Gilberto Carlos Dominguez
	
"""

import numpy as np
import perceptron 
import adaline
import preprocessing


np.random.seed(42)

class MLP:
	def __init__(self, hidden_layer_sizes, alpha, mode): 
		self.alpha = alpha #	learning rate
		self.hidden_layer_sizes = hidden_layer_sizes # tupla tal que el elemento i indica el numero de neuronas en la capa oculta i
		self.mode = mode #mode es para saber si se hará regresion o clasificación
		self.hidden_weights = self.initialize_weights() # lista de matrices que son los pesos entre cada capa
		#self.input = input

	#if self.mode == 1:
	def initialize_weights(self,):
		weights = []
		#n_neurons = self.hidden_layer_sizes[0]
		#w_input = 0.02 * np.random.random_sample() - 0.01
		for n_neurons in self.hidden_layer_sizes:	
			w = 0.02 * np.random.random_sample(n_neurons) - 0.01
			#theta = 1
			weights.append(w)
		return weights

	def fit(self, X, y):
		w_input = 0.02 * np.random.random_sample(len(X.values[0])) - 0.01





if __name__ == '__main__':

	#layer = []
	#alpha = 0.01
	#epochs = 10
	#for i in range(11):
	#	new = adaline.Adaline(alpha, epochs)
	#	layer.append(new)
	filename = 'housing.data'
	PATH = 'data/'
	df = preprocessing.estandarizar_datos(preprocessing.clean_ugly_dataset(PATH+filename))
	sizes = (10, 15)
	alpha = 0.01
	mode = 1
	mlp = MLP(sizes, alpha,mode)


