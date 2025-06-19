# Ejercicio 1 - Usa math para calcular la raiz cuadrada de un numero.
import math 

print(f"La raiz de cuadrada es: ",math.sqrt(16))
# Ejercicio 2 - Simula un dado que devuelve un numero del 1 al 6 con random.
import random
print("El dado quedo en: ",random.randint(1,6))
# Ejercicio 3 - Mostra la fecha y hora actual con datetime.
import datetime 

ahora = datetime.datetime.now()
print(ahora)
print(ahora.year, ahora.month, ahora.day)
# Ejercicio 4 - Pausa el programa 3 segundos antes de mostrar un mensaje con time.
import time
print("Empieza...")
time.sleep(3)
print("Fin!")
# Ejercicio 5 - Crea un archivo .py con una funcion y usalo desde otro.
# Archivo llamando micalculadora.py
def sumar(a, b):
    return a + b

# Otro archivo
import micalculadora
print(micalculadora.samar(3,4))
