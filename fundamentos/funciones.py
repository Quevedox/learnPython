# Ejercicio 1 - Crea una funcion que reciba tu nombre y te salude.
def saludar(nombre):
    print("Hola", nombre)
saludar("Guillermo")
# Ejercicio 2 - Escribi una funcion que reciba dos numeros y devuelva su producto.
def suma(a, b):
    return a + b
    
resultado = suma(3, 5)
print(resultado)
# Ejercicio 3 - Hace una funcion que reciba una nota y diga si esta aprobada (>=6).

def examen():
    nota = float(input("Cual es tu nota? "))
    if nota >= 6:
        print("Exonerado")
    else:
        print("No aprobado")

examen()
# Ejercicio 4 - Defini una funcion que reciba un numero y diga si es par o impar.
def par():
    numero = float(input("Cual numero quiere ingresar? "))
    if numero % 2 == 0:
        print(f"{numero} es un numero par")
    else:
        print(f"{numero} es impar")

par()
# Ejercicio 5 - Escribi una funcion que reciba una lista de numeros y devuelva la suma total.
def procesar_lista():
    entrada = input("Ingresa los numeros separados por espacio: ")
    texto_a_lista = entrada.split()
    numeros = [float(n) for n in texto_a_lista]
    suma_total = sum(numeros)
    print("La suma de la lista es:", suma_total)

procesar_lista()