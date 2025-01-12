lenguajes = ["Python", "Java", "Golang"]

print(lenguajes)

lista = [1, 2.0, True, "python", 1]

print(lista)

print(lenguajes[0]) # Acceder a un elemento de la lista a través de su índice
print(len(lenguajes)) # Imprime longitud de la lista
print(lenguajes[-1]) # Acceder al último elemento de la lista
print(lenguajes[0:2]) # Acceder a un rango de elementos de la lista

programacion = [lenguajes, "dedicacion", "practica"]

print(programacion)

print(programacion[0][0]) # Acceder a un elemento de una lista anidada

lenguajes[0] = "Dart"

print(lenguajes)

lenguajes.append("Python") # Agregar un elemento al final de la lista

print(lenguajes)

otros_lenguajes = ["C", "C++", "Ruby"]

lenguajes.extend(otros_lenguajes) # Agregar una lista a otra lista

print(lenguajes)

lenguajes.append(otros_lenguajes) # Agregar una lista a otra lista

print(lenguajes)