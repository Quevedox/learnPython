# Ejercico 1 - Crea una clase Persona con nombre y edad, y un metodo presentarse.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Datos de prueba
persona1 = Persona("Guillermo", 23)
persona1.saludar()

# Ejercicio 2 - Hace una clase Libro con titulo y autor, que muestre su descripcion.
class Libro:
    def __init__(self, titulo, autor, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"El libro {self.titulo} con el autor {self.autor} y su descripcion {self.descripcion}")

# Datos de prueba
Libro1 = Libro("El camino del lobo", "Jordan", "Domina la persuacion")
Libro1.mostrar_info()

# Ejercicio 3 - Simula una clase CuentaBancaria con metodos para depositar y retirar
class CuentaBancaria:
    def __init__(self):
        self._saldo = 0

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser mayor que cero")
        else:
            self._saldo += monto
    def retirar(self, monto):
        if monto > self._saldo:
            print("Saldo insuficiente")
        else:
            self._saldo -= monto

    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")

# Ejercicio 4 - Implementa una clase Animal y una clase Gato que herede de ella y sobreescriba un metodo.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Ejercicio 5 - Crea una clase Rectangulo que calcule su area y perimetro
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

rectangulo1 = Rectangulo(6, 4)
print("Perimetro: ", rectangulo1.perimetro())

rectangulo2 = Rectangulo(4, 5)
print("Area: ", rectangulo2.area())
        