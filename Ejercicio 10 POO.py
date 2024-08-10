#Ejercicio 10
def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i 
        return resultado 
numero = 14
resultado = factorial(numero)
print(f"El factorial del numero dado  {numero} es {resultado}")