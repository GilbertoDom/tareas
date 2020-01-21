#! /usr/bin/env python3
#-*- coding:utf-8 -*-

# Inteligencia Artificial
# Proyecto 6; Satisfacción de restricciones; Criptoaritmética
# Gilberto Carlos Domínguez Aguilar (417097202)
# 
#

#libraries
# import numpy as np
# import random 
from sympy import symbols


class CSP:
    def __init__(self, variables, constrains):
        """
        Constructor; 
        Parameters:
            variables:  A set of n variables
            constrains: A set of constrains 
        """
        self.vars = variables # n variables
        self.constrains = constrains # n domains
        # self.possible_complete_assignments = max([len(i) for i in self.domains]) # 0(d^n)

# def succesor(state):



# def expand(variable):
#     # print(state)
#     s = {}
#     for (variable_n, value_domain) in variable.items():
#         for val, domain in value_domain.items():
#             childs = [gen_state( value=x) for x in domain]
    
    

domain = [0,1,2,3,4,5,6,7,8,9]

# initial state
state  = {
    "T": {"value": 0, "domain": domain},
    "W": {"value": 0, "domain": domain},
    "O": {"value": 0, "domain": domain},
    "F": {"value": 0, "domain": domain},
    "U": {"value": 0, "domain": domain},
    "R": {"value": 0, "domain": domain},
    "X1": {"value":0, "domain":[0,1]},
    "X2": {"value":0, "domain":[0,1]},
    "X3": {"value":0, "domain":[0,1]},
     }
constrains = 

# for depth first we use a stack or LIFO
assignment = []
# assignment.append(state)


for (variable_n, value_domain) in variable.items():
    for val, domain in value_domain.items():
        childs = [gen_state( value=x) for x in domain]


# 