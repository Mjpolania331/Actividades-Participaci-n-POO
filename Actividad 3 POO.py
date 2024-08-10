#Punto 1
class Vehiculo:
    def __init__(self, Velocidadmax, Kilometraje):
        self.Velocidadmax = Velocidadmax
        self.Kilometraje = Kilometraje
#Aqui verificamos que la clase creada esta correcta
#Vehiculo = Vehiculo(100,10000)
#print(vehiculo.kilometraje)

#Punto 2
import math 
class Punto:
    def __init__(self, x, y, distancia):
        self.x = x
        self.y = y
        self.distancia = distancia

#Punto 3
def mostrar(self,x,y):
    print( x, y)

def mover(self,nueva_x,nueva_y):
    self.x = nueva_x
    self.y = nueva_y

def calcular_distancia(self,nueva_x,nueva_y,z,p):
    self.distancia = math.sqrt((nueva_x-nueva_y)**2+(z-p)**2)

#Punto 4
class rectangulo:
def __init__(self, p1, p2):
     self.p1 = p1 #p1 y p2 son las coordenadas de las esquinas opuestas del rectangulo
     self.p2 = p2 

def calcular_perimetro(self):
    #Calculamos la longitud de los lados 
    Lado1 = abs(self.p1[0] - self.p2[0])
    Lado2 = abs(self.p1[1] - self.p2[1])
    #Calculamos el perimetro
    return 2 * (lado1 + lado2)

def calcular_area(self):
    #Calculamos la longitud de los lados
    Lado1 = abs(self.p1[0] - self.p2[0])
    Lado2 = abs(self.p1[1] - self.p2[1])
    #Calculamos el area
    return lado1 * lado2

def es_cuadrado(self):
    #Un rectangulo es un cuadrado si ambos lados son iguales
    Lado1 = abs(self.p1[0] - self.p2[0])
    Lado2 = abs(self.p1[1] - self.p2[1])
    return lado1 == lado2

#Punto 5
class circulo:
def __init__(self, centro, radio):
    self.centro = centro
    self.radio = radio

def area(self,radio):
    self.area= math.pi * self.radio ** 2

def perimetro(self,radio):
    self.perimetro= 2 * math.pri * self.radio

def punto_pertenece(self, punto):
    distancia_al_centro = math.sqrt((punto[0] - self.centro[0])** 2 + (punto[1]- self.centro[1])**2) 
    return distancia_al_centro <= self.radio

#Punto 6
class carta:
#se definen las constantes antes que todo
ROSADO = "Rosado"
MORADO = "Morado"
AZUL = "Azul"
AMARILLO = "Amarillo"
def __init__(self, valor, pinta):
    self.valor = valor
    if pinta in {carta, ROSADO, carta, MORADO, carta, AZUL, carta, Amarillo}:
        self.pinta= pinta

#Punto 7
class CuentaBancaria:
def __init__(self, ncuenta, propietarios, balance):
    self.ncuenta = ncuenta
    self.propietarios = propietarios
    self.balance = balance

#Punto 8
def depositar (self, balance, deposito):
    self.balance += deposito

#Punto 9
def retirar(self,balance,retiro):
    if retiro <= self.balance:
        self.balance -= retiro
    else:
        print("Fondos insuficientes")

#Punto 10
def cuota_manejo( self, balance):
    self.balance -= self.balance * 0.02

#Punto 11
def mostrar_detalles (ncuenta, propietarios, balance):
    print("ncuenta, propietarios, balance")