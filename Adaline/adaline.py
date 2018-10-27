#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Adaptive Linear Neuron, (ADALINE)

"""

import numpy as np

class Adaline:
    def __init__(self, alpha, epochs): # inicializador
        self.alpha = alpha # Tasa de aprendizaje entre (0,1)
        self.epochs = epochs # Numero de epocas 
        self.theta = None # umbral 
        self.w = None # vector de pesos

        
    def fit(self, X, y): # entrenamiento
        np.random.seed(42)
        n = len(X.keys())
        w = 0.02 * np.random.random_sample(n) - 0.01
        #print(w)
        theta = 1
        err_history = []
        sq_errs = []
        for epoch in range(self.epochs):
            correctos = 0
            for pattrn, dx in zip(X.values, y.values):
                suma_ponderada = self.net_input(pattrn, w,)
                #rint(suma_ponderada)
                salida = self.activation(suma_ponderada)
                #print(salida)
                if salida == dx:
                    correctos += 1
                else:

                    w, se = self.learn(salida, pattrn, w, dx)
                    sq_errs.append(se)
            #print
            mse = sum(sq_errs)/len(sq_errs)
            err_history.append(mse)
            #print()
            print("Epoch {}".format(epoch+1,)) #(correctos/len(X)*100)))
            print('Mean squared error global: {}'.format(mse))
            self.w = w
        #self.theta = theta

        return err_history


    def net_input(self, pattern, w): # suma ponderada
        #x = np.append(pattern, [1])
        #wsub = np.append(w, [theta])
        
        suma_ponderada = np.dot(pattern.T, w)
        return suma_ponderada


    def activation(self, suma): # Función de activación
        return suma


#       if suma > 0:
#           return 1
#       else:
#           return -1


    def learn(self, salida, pattern, weight, dx): # función de aprendizaje
        
        error = dx - salida
        #error = np.array(error, dtype=np.float64)
        #print (error)
        #print(pattern)
        #print(weight)
        #xsub = np.array([])
        wsub = np.array([])
        l=[]
        #print(error)
        for x, w in zip(pattern, weight):
            #delta = np.array(self.alpha, dtype=np.float64) * error * x
            delta = self.alpha * error * x
            w1 = w + delta
            l.append(w1)
        wsub = np.append(wsub, l)

        #print(error)
        #print(wsub)
        return wsub, error*error


    def predict(self, X): #validacion
        predicted = []
        for x in X.values:
            #predicted_c = self.f(self.net_input(x, self.w, self.theta))
            pred = self.activation(self.net_input(x, self.w)) 
            predicted.append(predicted_c)

        return predicted


#EOF