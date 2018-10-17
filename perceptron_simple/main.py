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
import ova
import matplotlib.pyplot as plt


def build_dataframes(train_i, test_i, df):
	#np.random.seed(42)
	#df = pd.read_csv(filename)
	#msk = np.random.rand(len(df)) < 0.7


	train = []
	test = []

	
	for i in train_i:
		instance = df.loc[i].values
		#print(type(instance))
		train.append(instance)

	for i in test_i:
		instance = df.loc[i].values
		test.append(instance)

	#print (train[0], train[1], train[2], train[3], train[4], train[5], train[6], train[7])
	#print(train)
	columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid', 'class']
	train = pd.DataFrame(train, columns=columns)
	test =  pd.DataFrame(test, columns=columns)	

	#print(train.shape)
	#print(train.keys())
	#print(train.iloc[0,0])
	#print(train.iloc[:,:-1])

	return train, test

#	X_train = df[msk]
#	Y_train = X_train["class"]
#	X_train = X_train.drop(axis=1, columns='class')
#	t_w_class = df[~msk]
#	X_test = t_w_class.drop(axis=1, columns='class')
#	test_class = t_w_class.iloc[:,-1]

#	return X_train, Y_train, X_test, test_class


def frag_in_k(df, k):
	frag_size = len(df)//k
	res = len(df)%k
	rperm = np.random.permutation(df.index.values)
	c = frag_size
	fragments = {}
	last = 0
	for i in range(k):
		if i == k-1:
			if res != 0:
				c += res
				fragment = rperm[last:c]		
				fragments[i+1] = fragment
			else:
				fragment = rperm[last:c]
				fragments[i+1] = fragment
		else:				
			fragment = rperm[last:c]
			fragments[i+1] = fragment
			last = c
			c += frag_size

	return fragments

			
	#eturn flist

def cross_v(df, k):
	fragments = frag_in_k(df, k)
	used = []

	#for key, frag in fragments.items():
	#train = []
	for i in range(1,k+1):
		train_i = []
		test_i = fragments[i]	
		l = [n for n in range(1, k+1)]
		l.remove(i)
		#print(str(l)+'ww')
		for n in l:
			train_i = np.append(train_i, fragments[n])
		#print(train_i)

		train, test = build_dataframes(train_i, test_i, df)
		
		#print(train.shape)
		#print(test.shape)
		#print(train)
		X_train = train.iloc[:,:-1]
		y_train = train.iloc[:,-1]
		X_test = test.iloc[:,:-1]
		y_real = test.iloc[:,-1]

		yield X_train, y_train, X_test, y_real
		#print(test)
		#print()
		#print(train)



	#return fragments



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
	#s = "Resultados del clasificador en la validacion :\n\tExactitud: {:0.2f}%\n\tSensibilidad : {:0.2f}%\n\tFalsa Alarma: {:0.2f}%\n\tPrecisión: {:0.2f}%\n\tF1 Score: {:0.2f}\n".format( accuaracy*100, recall*100, false_alarm*100, precision*100, f1score)
	s = "Resultados del clasificador en la validacion :\n\tExactitud: {:0.2f}%".format(accuaracy*100)
	print()
	print (s)
	print()

	return accuaracy

def plot_accs(accs, epochs, name):
	
	e_count = np.linspace(1, len(accs), len(accs))
	plt.plot(e_count,accs, label=name,) #ylim=(0,1) )
		#epoch += 1

if __name__ == '__main__':
	files = ["Iris-setosa", "Iris-virginica", "Iris-versicolor"]
	#alpha = 0.3
	#epochs = 10
	#alpha = 0.45653
	#epochs = 20
	#alpha = 0.5653
	#epochs = 30
	#alpha = 0.23464
	#epochs = 70
	alpha = 0.5
	epochs = 70

	k = 5
	designated = {}
	for cnum in range(len(files)):
		print()
		print('Ahora entrenando con: {}'.format(files[cnum]))
		print()
		df = pd.read_csv(files[cnum])
		cross = cross_v(df, k)
		weights = {}
		accuracies = {}
		for ev in range(k):# son k perceptrones por cada valor de la clase o sea k * cnum total de perceptrones
			clf = perceptron.Perceptron(alpha=alpha, epochs=epochs)
			#X_train, y, X_test, real_class = cross_v(df, k)
			#cross = cross_v(df, k)
			X_train, y, X_test, real_class = next(cross)
			#print(X_train, y, X_test, real_class)
			punct = clf.fit(X_train, y)
			
			predicted = clf.predict(X_test)
			acc = evaluate(predicted, real_class)
			#evaluate(predicted, real_class)
			weights[acc] = (clf.w, clf.theta)
			accuracies[acc]= punct

		#print(accuracies)
		#plot_accs(accuracies, epochs, files[cnum])
		best = max(weights.keys())
		designated[files[cnum]] = weights[best]
		plot_accs(accuracies[best], epochs, files[cnum])
	#print(designated)
	df = pd.read_csv(files[0], )#names = ["sep_len", "sep_wid", "pet_len", "pet_wid", 'clase'])
	df = df.iloc[:,:-1]
	#print(df.head())

	#alpha, epochs = 0.23343, 20

	predicted = ova.OneVsAll(designated, df)

	df = pd.read_csv('iris.data.txt', names = ["sep_len", "sep_wid", "pet_len", "pet_wid", 'clase'])
	df = df.iloc[:,-1]
	ova.evaluate_ova(predicted, df)



##################### Ploting  #####################3
	plt.legend()
	plt.xlabel('Epochs')
	plt.ylabel('Accuaracy')
	plt.grid()
	plt.ylim(0,1.05)
	plt.title('Performance throught the epochs\nof the perceptron with the highest accuaracy in prediction')
	plt.show()
	#df = pd.read_csv(files[1])
	#f = cross_v(df, k)




#EOF