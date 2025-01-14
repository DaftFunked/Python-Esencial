lenguaje = {
    "nombre": "Python",
    "creador": "Guido van Rossum"
}
for key in lenguaje: # Iterar el diccionario
    print("llave:", key) # Imprimir la llave
    print("valor:", lenguaje[key]) # Imprimir el valor
    
for element in lenguaje.keys(): # Iterar las llaves del diccionario
    print(element) # Imprimir la llave
    
for element in lenguaje.values(): # Iterar los valores del diccionario
    print(element) # Imprimir el valor
    
for key, value  in lenguaje.items(): # Iterar las llaves y valores del diccionario
    print(key, value) # Imprimir la llave y el valor
    
for element in lenguaje.items(): # Iterar las llaves y valores del diccionario
    print(element) # Imprimir la llave y el valor