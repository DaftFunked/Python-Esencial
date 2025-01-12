set1 = {1,2,3}

print(set1)

set2 = {1,1,1,2,3,4,5}

print(set2)

set3 = {1,2.0,"texto"}

print(set3)

set1.add(4) # Agregar un elemento al conjunto

print(set1)

set1.update([4,5,6]) # Agregar varios elementos al conjunto

print(set1)

print(len(set1)) # Devuelve la cantidad de elementos del conjunto

set1.discard(2) # Elimina un elemento del conjunto si existe

print(set1)

set1.remove(3) # Elimina un elemento del conjunto si existe, si no existe lanza un error

print(set1)

set1.clear() # Elimina todos los elementos del conjunto

print(set1)