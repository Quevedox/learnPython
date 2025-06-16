sexo = "M"
nota = float(input("Ingrese su nota: "))

if sexo == "M":
    print("Sos Hombre")
else:
    print("Sos mujer")

if 0 <= nota <= 10:
    if nota >= 9:
        print("Excelente")
    elif 6 < nota <= 8:
        print("Bien")
    else:
        print("Desaprobado")
else:
    print("Nota invalida")