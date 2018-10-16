#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Perceptron Simple

"""

import numpy as np

class Perceptron:
	def __init__(self, alpha, epochs): # inicializador
		self.alpha = alpha # Tasa de aprendizaje entre (0,1)
		self.epochs = epochs # Numero de epocas 
		self.theta = None # umbral 
		self.w = None # vector de pesos

		
	def fit(self, X, y): # entrenamiento
		np.random.seed(42)
		n = len(X.keys())
		w = 0.02 * np.random.random_sample(n) - 0.01
		theta = 1

		for epoch in range(self.epochs):
			correctos = 0
			for pattrn, dx in zip(X.values, y.values):
				suma_ponderada = self.net_input(pattrn, w, theta)
				y_obtenida = self.f(suma_ponderada)
				if y_obtenida == dx:
					correctos += 1
				else:
					w, theta = self.learn(pattrn, w, theta, dx)

			print()
			print("Epoch {}\tExactitud: {:0.2f}%".format(epoch+1, (correctos/len(X)*100)))
		self.w = w
		self.theta = theta



	def net_input(self, pattern, w, theta): # suma ponderada
		x = np.append(pattern, [1])
		wsub = np.append(w, [theta])
		suma_ponderada = np.dot(x.T, wsub)
		return suma_ponderada


	def f(self, suma): # Función de activación
		if suma > 0:
			return 1
		else:
			return -1


	def learn(self, x, w, theta, dx): # función de aprendizaje
		if dx == 1:
			w2 = w + (self.alpha*x)
			theta2 = theta + (self.alpha*dx)
		else:
			w2 = w - (self.alpha*x)
			theta2 = theta + (self.alpha*dx)

		return w2, theta2


	def predict(self, X): #validacion

		predicted = []
		for x in X.values:
			predicted_c = self.f(self.net_input(x, self.w, self.theta))
			predicted.append(predicted_c)

		return predicted
