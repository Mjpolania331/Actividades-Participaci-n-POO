#Ejercicio 9
filas = 5
columnas = 4
matriz = []
for i in range (filas):
    fila = []
    for j in range (columnas):
        numeros_aleatorios = random.randint(2,50)
        fila.append(numeros_aleatorios)
matriz.append(fila)
