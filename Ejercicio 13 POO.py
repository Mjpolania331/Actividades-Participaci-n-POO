#Ejercicio 13
Primer_numero= float(input("Ingrese el primer numero:"))
Segundo_numero= float(input("Ingrese el segundo numero:"))
suma= Primer_numero + Segundo_numero
resta= Primer_numero - Segundo_numero
Multiplicacion = Primer_numero * Segundo_numero

if Segundo_numero != 0:
    division = Primer_numero / Segundo_numero
else:
    division = "No es posible realizar la division entre 0"

print(f"\nresultados:")
print(f"Suma : {suma}")
print(f"Resta : {resta}")
print(f"Multiplicacion: {Multiplicacion}")
print(f"Division: {Division}")


