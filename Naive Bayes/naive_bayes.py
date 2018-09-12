#-*- coding:utf-8 -*-
#Mineria de Datos
#Naive Bayes Implement
#Gilberto Carlos Domínguez Aguilar
"""
-------------naive_bayes.py------------

Implementacion del algoritmo Naive Bayes para la clasde de mineria de datos.
El programa recibe dos archivos csv, train y test, la clase debe estar
en la ultima columna y los datos deben ser categoricos.

"""
import pandas as pd
import numpy as np
import argparse


class Classifier:
    def __init__(self, training_set, testing_set):
        self.train_name = training_set
        self.test_name = testing_set
        self.likelihoods = {}
        self.traindf = self.build_data_frame(training_set)
        self.testdf = self.build_data_frame(testing_set)
        self.hipothesis = []
        self.attrib_search = {}
        self.prior_ps = []

    def build_data_frame(self, trainset):
        """
        construyendo dataframe de pandas a partir archivos csv
        """
        df = pd.read_csv(trainset, sep=',')

        return df

    def learn(self):
        df = self.traindf
        classdfname = list(df)[-1] # nombre de la clase para buscarla en el df, siempre debe estar en la ultima columna
        classdf = df[classdfname] # construyendo dataframe de la clase
        class_occurrences = self.val_count(classdf) # lista de ocurrencias de los valores de la clase
        self.hipothesis = list(class_occurrences.keys())
        prior_ps = {}
        for key, val in class_occurrences.items():
            prior = float(val)/float(len(classdf))
            prior_ps[key] = prior # probabilidad a priori de las hipotesis

        self.prior_ps = prior_ps
        attrbs = list(df.keys())
        del(attrbs[-1])

        likelihoods = {} #almacenará los valores de las probabilidades condicionales (likelihoods)
        attrib_search = {}
        for attribute in attrbs:
            attrdf = df[attribute]
            values_occurrences  = self.val_count(attrdf)

            for hip, h_count in class_occurrences.items():
                conditional_p = {}
                max_so_far = 0
                max_vname = ''
                for value in values_occurrences.keys():
                    max_ = 0
                    val_hip_count = self.and_search(df, attribute, value, hip) # contando cuantas instancias con el atributo a1 = valor v1 dada la hipotesis
                    likelihood = float(val_hip_count)/float(h_count) #calculando el likelihood como # de instancias resultado del and entre # de instancias de la hipotesis
                    attrib_search[value] = attribute
                    conditional_p[value] = likelihood
                name_of_p = "{}:{}".format(attribute, hip )
                likelihoods[name_of_p] = conditional_p

        self.attrib_search = attrib_search
        self.likelihoods = likelihoods


    def test(self):
        df = self.testdf
        classes_ = self.hipothesis
        classified = []
        instances = self.get_instance(df)
        attrbs = list(df.keys())

        for instance in instances:
            instance_ps = {}
            for class_ in classes_:
                instance_ps[class_] = [self.prior_ps[class_]]
                for value in instance:
                     instance_ps[class_].append(self.get_likelihood(value, class_))

            max = 0
            cl = None
            for key, val in instance_ps.items():
                p = self.multiplyList(val)
                if p > max:
                    max = p
                    cl = key
            classified.append(cl)
        print(classified)


    def multiplyList(self, myList) :
        # Multiply elements one by one
        result = 1.
        for x in myList:
            result = result * x
        return result


    def get_likelihood(self, val, hip):
        att = self.attrib_search[val]
        L = self.likelihoods["{}:{}".format(att, hip)][val]
        return L

    def get_instance(self, df):
        for instance in df.values:
            yield instance

    def and_search(self, df, attrib_name, attrib_val, hip):
        coln = df.columns.get_loc(attrib_name)
        count  = 0
        for i in range(len(df)):
            a_val = df.iloc[i][coln]
            c_val = df.iloc[i][-1]
            if a_val == attrib_val and c_val == hip:
                count += 1
        return count


    def val_count(self, df):
        D = {}
        l_of_vals = list(set(df.values))
        l_of_vals = self.remove_nan(l_of_vals)
        for key in l_of_vals:
            D[key] = 0
            for value in df:
                if value == key:
                    D[key] += 1
        return D


    def remove_nan(self, l_of_values):
        L = []
        for val in l_of_values:
            if val == val:
                L.append(val)
        return L


    def print_learned_vals(self):
        for key, val in self.likelihoods.items():
            print("Probabilities of {}".format(key))
            for tag, v in val.items():
                print("{}\t\t{}".format(tag, v))
            print ()


def main(training, testing):
    myclassifier = Classifier(training, testing)
    myclassifier.learn()
    #myclassifier.print_learned_vals()
    myclassifier.test()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Naive Bayes Algorithm Implement in Python.')
    parser.add_argument('training', help='Training set name e.g. (example.csv)')
    parser.add_argument('test', help='Test set name (also csv)')
    args = parser.parse_args()
    training_name = args.training
    testing_name = args.test

    main(training_name, testing_name)
