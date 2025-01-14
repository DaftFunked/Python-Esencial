for letra in "Texto": # Recorre cada letra de la palabra "Texto"
    print(letra) # Imprime cada letra
    
lenguajes = ["Python", "Java", "Golang"] # Lista de lenguajes
for elemento in lenguajes: # Recorre cada elemento de la lista
    """print(elemento) # Imprime cada elemento
    if elemento == "Java": # Si el elemento es "Java"
        break # Rompe el ciclo"""
    if elemento == "Java": # Si el elemento es "Java"
        continue # Continua con la siguiente iteración
    print(elemento) # Imprime
    
for element in range(5): # Recorre los números del 0 al 4
    print(element) # Imprime los números del 0 al 4
    
for element in range(1, 5): # Recorre los números del 1 al 4
    print(element) # Imprime los números del 1 al 4