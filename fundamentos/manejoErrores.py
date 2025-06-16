# Ejercicio 1 - Pedi dos numeros al usuario y mostra el cociente, controlado division por cero.
try:
    def division(a, b):
        return a / b
    resultado = division(10, 0)
    print(resultado)
except ZeroDivisionError:
    print("No se puede divir entre cero")

# Ejercicio 2 - Hace un programa que pida una edad y controle que sea numero.
try:
    edad = float(input("Ingrese su edad"))
except ValueError:
    print("Solo son validos numeros enteros")

# Ejercicio 3 - Intenta acceder a una clave de diccionario que no existe, usa try/except para menajerlo.
try:
    diccionario = {
        "nombre": 'Guillermo',
        "edad": 18
    }
    print(diccionario["apellido"])
except KeyError:
    print("La clave no existe en el diccionario")
# Ejercicio 4 - Abri un archivo que no existe y atrapa la excepcion.
try:
    with open("archivo_que_no_existe.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe")
# Ejercicio 5 - Escribi un try/except/else/finally que sume dos numeros.
try:
    a = int(input("Primer valor: "))
    b = int(input("Segundo valor: "))
    resultado = a + b
except ValueError:
    print("Debes ingresar solo numeros.")
else:
    print("Resultado:", resultado)
finally:  
    print("Fin del calculo.")