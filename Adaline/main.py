#! /user/bin/env python3
# -*- coding:utf-8 -*-

"""
Tecnologías p/ la informacion en Ciencias
Redes Neuronales Artificiales 
Gilberto Carlos Dominguez Aguilar
Adaptive Linear Neuron (ADALINE), main Script

"""
import preprocessing as pre
from adaline import Adaline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def build_dataframes(train_i, test_i, df):
    train = []
    test = []

    for i in train_i:
        instance = df.loc[i].values
        train.append(instance)

    for i in test_i:
        instance = df.loc[i].values
        test.append(instance)

    #columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid', 'class']
    columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'DIS','AGE', 'RM', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV' ]
    train = pd.DataFrame(train, columns=columns)
    test =  pd.DataFrame(test, columns=columns) 


    return train, test


def build_test(df):
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    test = df[~msk]

    X_train = train.iloc[:,:-1]
    y_train = train.iloc[:,-1]
    X_test = test.iloc[:,:-1]
    y_real = test.iloc[:,-1]

    return X_train, y_train, X_test, y_real


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


def cross_v(df, k):
    fragments = frag_in_k(df, k)
    #used = []


    for i in range(1,k+1):
        train_i = []
        test_i = fragments[i]   
        l = [n for n in range(1, k+1)]
        l.remove(i)

        for n in l:
            train_i = np.append(train_i, fragments[n])


        train, test = build_dataframes(train_i, test_i, df)

        X_train = train.iloc[:,:-1]
        y_train = train.iloc[:,-1]
        X_test = test.iloc[:,:-1]
        y_real = test.iloc[:,-1]

        yield X_train, y_train, X_test, y_real

def plot_error(history, epochs, fold):
    
    e_count = np.linspace(1, len(history), len(history))
    plt.plot(e_count,history, label='fold {}'.format(fold+1)) 

def plot_error_lr(history, epochs, lr):
    e_count = np.linspace(1, len(history), len(history))
    plt.plot(e_count,history, label='alpha: {}'.format(lr))


if __name__ == '__main__':


    np.random.seed(42)

    alpha = 0.01
    epochs = 20
    k = 5


    filename = 'housing.data'
    df = pre.clean_ugly_dataset(filename)
    df = pre.estandarizar_datos(df)
    cross = cross_v(df, k)
    clf = Adaline(alpha, epochs)

    #X_train, y_train, X_test, y_real = next(cross)
    #istory_ = clf.fit(X_train, y_train)
        

    for fold in range(k):

        X_train, y_train, X_test, y_real = next(cross)
        #print(X_train)
        print()
        print('Fold {}'.format(fold))
        print()
        history_ = clf.fit(X_train, y_train)


        plot_error(history_, epochs, fold)


    plt.legend()
    plt.xlabel('Epochs')
    plt.ylabel('Mean Squared Error (mse)')
    plt.grid()
    plt.title('Adaline learning curve with\nK-fold Cross V, k = 5, alpha=0.01')
    plt.show()

    w = clf.w
    X_train, y, X_test, y_real = build_test(df)
    #print(w)
    rates = [0.1, 0.01, 0.001, 0.0001]
    #cross = cross_v(df, k)
    
    for lr in rates:
        cl = Adaline(lr, epochs)
        cl.w = w
        print()
        print('now alpha = {}'.format(lr))
        hist = cl.fit(X_train, y)
        plot_error_lr(hist, epochs, lr)


    plt.legend()
    plt.xlabel('Epochs')
    plt.ylabel('Mean Squared Error (mse)')
    plt.ylim(0,1)
    plt.grid()
    plt.title('Adaline learning curves with\nvariable learning rate (alpha)')
    plt.show()

