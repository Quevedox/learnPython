# Ejercicio 1 - Pedi nombre y edad al usuario, mostra el año en que nacio.
def calcular_nacimiento():
    from datetime import datetime
    nombre = input("Cual es tu nombre?: ")
    edad = int(input("Cual es tu edad?: "))
    nacimiento = datetime.now().year - edad
    print(nombre, ", tu año de nacimiento es: ", nacimiento)

calcular_nacimiento()
# Ejercicio 2 - Solicita 2 numeros y mostra el resultado de la suma, producto y cociente.
numero1 = input("Ingrese primer numero: ")
numero2 = input("Ingrese segundo numero: ")

operacion = input("Ingrese operacion: suma, producto, cociente: ")
if operacion == "suma":
    resultado = numero1 + numero2
    print("El resultado de la suma es: ", resultado)

elif operacion == "producto":
    resultado = numero1 * numero2
    print("El resultado del producto es: ", resultado)

elif operacion == "cociente":
    resultado = numero1 / numero2
    print("El resultado del cociente es: ", resultado)

else: 
    print("Ingrese una operacion valida")
# Ejercicio 3 - Pedi una palabra y mostra cuantas letras tiene.

palabra = str(input("Ingresa una palabra y te dire cuantas letras tiene: "))
print("La palabra tiene", len(palabra), "letras.")
# Ejercicio 4 - Pedi un numero decimal y redondea a 2 decimales.

numero_decimal = float(input("Ingrese un numero decimal: "))
print("El numero redondeado es: ", round(numero_decimal))
# Ejercicio 5 - Pedi nombre y apellido, mostralo en mayusculas.

nombre = input("Ingrese un nombre: ")
apellido = input("Ingrese un apellido: ")

print("Tu nombre es:", nombre.upper(), "y tu apellido \n", apellido.upper())