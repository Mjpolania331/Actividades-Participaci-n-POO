#Ejercicio 3
numeros=int(input("Ingrese los numeros aleatorios"))
valor_minimo=int(input("Ingrese el valor minimo de los numeros aleatorios"))
valor_maximo=int(input("Ingrese el valor maximo de los numeros aleatorios"))
valor_total=[random.randint(valor_minimo,valor_maximo)for in range (numeros)]
print("La lista de los numeros generados y el valor total:", valor_total)