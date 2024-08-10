#Ejercicio 14
lista= [20,25,30,35,40,45,50,55,60]
if not lista:
    media = 0
else:
    Suma= 0
    Cantidad= 0

for numero in lista:
    suma += numero
    Cantidad += 1

media = Suma / Cantidad
print (f"La media aritmética de esta lista es {media}")
    