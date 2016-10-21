# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:52:57 2016

@author: Sergio
"""
print "Este es un programa para encriptar frases. Consiste en indicar primero una frase a encriptar y luego dar dos valores numericos que sirvan para:" 
print "Primero alterar el orden de las palabras en la frase introducida"
print "Segundo cambia las letras por la letra en la posion del alfabeto que sea igual a la original + el numero indicado"
print "El alfabeto se considera de 26 letras y al llegar al fin comienza de nuevo"
x = raw_input ("Dime la frase a Encriptar \n")
lista = x.split ()
rango = len(lista)
print
print "Antes de introducir el numero para cambiar el orden entre palabras ten en cuenta que el numero debe estar entre 0 y ", len(lista)-1
orden = raw_input("¿Dime un numero para cambiar orden palabras:\n")
orden = int(orden)
claveLetras= raw_input ("¿Dime un numero para encriptar letras?   ")
claveLetras = int(claveLetras)
#print "tu clave usada para encritar las letras es:", claveLetras
fclaveLetras = claveLetras -((claveLetras/26) * 26)
#print lista
#print len(lista)
ListaN = []
for variable in lista:
    Indice = lista.index(variable)
    #print Indice
    Nindice = Indice + orden
    #print Nindice
    if Nindice >= len(lista):
        correccion = Nindice - len(lista)
        ListaN.insert(correccion,variable)
    elif Nindice < len(lista):
        ListaN.insert(Nindice,variable)          
#print " El nuevo orden es:", " ".join(ListaN)
#print ListaN   
#print ListaN
NuevaFrase = []
for word in ListaN:   
    variable = word
    Acumular = ""
    for letra in variable:
        Nletra = ord(letra) + fclaveLetras
        if Nletra < 122:
            nPalabras = str (chr(Nletra))
            Acumular = Acumular + nPalabras
            
        elif Nletra > 122:
            Cletra = (Nletra - 122) + 97
            nPalabras = str (chr(Cletra))
            Acumular = Acumular + nPalabras
            
    #print Acumular
    NuevaFrase.append(Acumular)
print "Tu frase Encriptada es:\n", " ".join(NuevaFrase)
