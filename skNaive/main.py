#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Minería de Datos 
Gilberto Carlos Dominguez Aguilar
Minería de datos con SK-Learn's Naive Bayes: Main script

"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import preprocessing


def parse_vetorizer(vname, vectorizer, body, clase):
	
	X = vectorizer.fit_transform(body)
	X_train, X_test, y_train, y_test = train_test_split(X, clase.values, test_size=0.30, random_state=10)
	clasificador = MultinomialNB()
	clasificador.fit(X_train, y_train)
	clasificacion = clasificador.predict(X_test)

	tp = 0
	fp = 0
	tn = 0
	fn = 0
	for prediccion, clase in zip(clasificacion, y_test):
		#correctos = 0
		if clase == 'spam':
			if prediccion == clase:
				tp += 1
			else:
				fn += 1
		else:
			if prediccion == clase:
				tn += 1
			else:
				fp += 1
	recall = tp / (tp+fn)
	false_alarm = fp / (fp+tn)
	precision = tp / (tp+fp)
	f1score = (2 * (recall*precision))/(recall+precision)
	accuaracy = (tp + tn) / (tp + fp + tn + fn)
	s = "Resultados del clasificador {}:\n\tExactitud: {:0.2f}%\n\tSensibilidad : {:0.2f}%\n\tFalsa Alarma: {:0.2f}%\n\tPrecisión: {:0.2f}%\n\tF1 Score: {:0.2f}\n".format(vname, accuaracy*100, recall*100, false_alarm*100, precision*100, f1score)
	print (s)

		
if __name__ == '__main__':

	clase = preprocessing.clase
	mensajes = preprocessing.body

	vect_with_sw = CountVectorizer(lowercase=True, decode_error='ignore')
	vect_wo_sw = CountVectorizer(stop_words='english', lowercase=True, decode_error='ignore')

	vect_min2 = CountVectorizer(stop_words='english', lowercase=True, decode_error='ignore', min_df=2)
	vect_min3 = CountVectorizer(stop_words='english', lowercase=True, decode_error='ignore', min_df=3)
	vect_min5 = CountVectorizer(stop_words='english', lowercase=True, decode_error='ignore', min_df=5)

	vecs = {'with stop words':vect_with_sw, 'w/o stop words':vect_wo_sw, 'min frec 2': vect_min2, 'min frec 3': vect_min3, 'min frec 5':vect_min5}

	for vname, vectorizer in vecs.items():
		parse_vetorizer(vname, vectorizer, mensajes, clase)



