#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import preprocessing




def create_numeric_representation(df):
	classes_values = list(set(df))
	new_vector = []
#	print(classes_values)
	
	for el in df.values:
		new_vector.append(classes_values.index(el)+1)

	ndf = pd.DataFrame(new_vector,)

	return ndf


"""
PATH='data/'
filename = 'iris-stndrzd.txt'

df = pd.read_csv(PATH+filename, sep=',')
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

y = create_numeric_representation(y)
"""

mlp = MLPRegressor(hidden_layer_sizes=(40, 25), 
					activation='relu',#'tanh',#'relu', 
					solver='sgd', 
					alpha=0.001,
					verbose=True)
"""
mlp = MLPClassifier(hidden_layer_sizes=(25,10), 
					activation='logistic', 
					solver='sgd', 
					alpha=0.001)
"""

df = preprocessing.clean_ugly_dataset('data/housing.data')
df = preprocessing.estandarizar_datos(df)

X, y = df.iloc[:,:-1], df.iloc[:,-1]


X_train, X_test, y_train, y_test = train_test_split(X, y, 
									test_size=0.33, random_state=42)

mlp.fit(X_train, y_train)
print(mlp.score(X_test, y_test))
