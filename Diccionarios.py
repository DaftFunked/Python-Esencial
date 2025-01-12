lenguaje = {
    "nombre": "Python",
    "creador": "Guido van Rossum",
}

print(lenguaje)

print(lenguaje["nombre"]) # Acceder a un elemento del diccionario a través de su clave
lenguaje["año lanzamiento"] = 1991 # Agregar un elemento al diccionario
print(lenguaje)

lenguaje["caracteristicas"] = ["sencillo", "fácil", "genial"] # Agregar una lista al diccionario
print(lenguaje)

lenguaje.items() # Devuelve una lista de tuplas con clave y valor
print(lenguaje.items())

lenguaje.keys() # Devuelve una lista con las claves del diccionario
print(lenguaje.keys())

lenguaje.values() # Devuelve una lista con los valores del diccionario
print(lenguaje.values())