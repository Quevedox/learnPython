# Ejercicio 1 - Crea una lista de 5 numeros, imprimi el primero y el ultimo
numero = [1,2,3,4,5]
print(numero[0])
print(numero[4])

# Ejercicio 2 - Modifica un elemento de una lista
lista_compras = ["Leche", "Carne picada", "Yogurt Griego"]
print(lista_compras)
lista_compras.append("Frutas")
print(lista_compras)
print("Fruta al final ya tengo, asi que hay que borrarlo")
lista_compras.pop()
print(lista_compras)

# Ejercicio 3 - Converti una lista a tupla y proba acceder a un valor
lista = [1,2,3]
print(tuple(lista))
lista.append("Juan")
print(tuple)
# Ejercicio 4 - Usa un set para eliminar duplicados de esta lista: [1,2,2,3,3,4]
lista = [1,2,2,3,3,4]
print(set(lista))
# Ejercicio 5 - Crea un diccionario con datos de una persona y mostra el valor de su edad
datos_persona = {
    "Nombre": "Guillermo",
    "Edad": 18
}
print(datos_persona)