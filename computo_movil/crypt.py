#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Programa de encripción 
# Gilberto Domínguez

def cambiar_letras(step,):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    crypt = {}
    decrypt = {}
    for x in alfabeto:
        new_pos = alfabeto.index(x) + step
        if new_pos >= len(alfabeto):
            new_pos = new_pos % len(alfabeto)
        # print(new_pos)
        crypt[x] = alfabeto[new_pos]
        for key,value in crypt.items():
            decrypt[value] = key
    
    return crypt, decrypt

def encriptar_msg(cadena, crypt):
    s = ''
    for letra in cadena:
        s += crypt[letra]
    return s
    
def desencriptar_msg(digest, crypt):
    s = ''
    for letra in digest:
        s += decrypt[letra]
    return s
        
    

if __name__ == '__main__':
    
    option = int(input("Seleccione una opción:\n\t1) encriptar\n\t2) desencriptar\n\t3) una corrida completa\n> "))
    if option == 1:
        
        steps = int(input("Diga el numero de corrimientos: "))
        cadena = input("ingrese su cadena: ").lower()
        crypt, decrypt = cambiar_letras(steps)
        digest = encriptar_msg(cadena, crypt)
        print('Su mensaje encriptado es: {}'.format(digest))
    elif option == 2:
        steps = int(input("Diga el numero de corrimientos: "))
        digest = input('Digite su mensaje encriptado: ')
        crypt, decrypt = cambiar_letras(steps)
        msg = desencriptar_msg(digest, decrypt)
        print('su mensaje desencriptado es: {}'.format(msg))
    else:
        steps = int(input("Diga el numero de corrimientos: "))
        cadena = input("ingrese su cadena: ").lower()
        crypt, decrypt = cambiar_letras(steps)
        digest = encriptar_msg(cadena, crypt)
        print('Su mensaje encriptado es: {}'.format(digest))
        msg = desencriptar_msg(digest, decrypt)
        print('su mensaje desencriptado es: {}'.format(msg))

    #print(cadena)

