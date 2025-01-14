lenguajes = ["Python", "Java", "Ruby", "JavaScript"] # Lista de lenguajes
for elemento in lenguajes: # Iterar la lista
    print(elemento) # Imprimir cada elemento de la lista
    
for index in range(len(lenguajes)): # Iterar la lista usando un índice
    print("indice", index) # Imprimir el índice
    print("elemento", lenguajes[index]) # Imprimir el elemento de la lista
    
i = 0
while i < len(lenguajes): # Iterar la lista usando un ciclo while
    print(lenguajes[i]) # Imprimir el elemento de la lista
    i += 1 # Incrementar el índice