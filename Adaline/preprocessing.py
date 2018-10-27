#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Adaptive Linear Neuron (ADALINE), preprocessing

"""
import pandas as pd


def clean_ugly_dataset(filename):
    columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'DIS','AGE', 'RM', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV' ]
    with open(filename, 'r') as f:
        data = f.readlines()

    clean_data = []
    for line in data:
        s = line.split(' ')
        clean_line = []
        for ch in s:
            try:
                val = float(ch)
                clean_line.append(val)
            except ValueError as e:
                continue
        clean_data.append(clean_line)

        df = pd.DataFrame(clean_data, columns=columns)

    return df


def estandarizar_datos(df):
    
    dflist = []
    for i in range(df.shape[1]):
        column = df.iloc[:, i]
        promedio = column.mean()
        desviacion = column.std()
        L = []
        for dato in column:
            z = (dato - promedio) / desviacion # estandarizacion no normalizacion
            L.append(z)
        dflist.append(L)
    ndf = pd.DataFrame(dflist)
    ndf = ndf.transpose()
    columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'DIS','AGE', 'RM', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV' ]

    return ndf



#filename = 'housing.data'
#columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'DIS','AGE', 'RM', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV' ]