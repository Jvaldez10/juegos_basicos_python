import random
# crea funcion


def adivina_el_numero(x):
    print("*****************************************")
    print("Empesemos a jugar a divina el numero !!!.")
    print("*****************************************")
    print("Trata de vencer adivina el numero .....")
    numero_aleatorio = random.randint(1, x)  # numero aleatorio entre 1 y x
    minumero = 0
    while minumero != numero_aleatorio:
        # usuario ingresa el numero
        minumero = input(f"adivina un numero entre 1 y {x}: ")
        minumero = int(minumero)
        #
        if minumero < numero_aleatorio:
            print("Intenta otra vez, este numero es muy pequeño.")
        elif minumero > numero_aleatorio:
            print("intenta otra vez, este numero es muy grande.")

    print(
        f"Felicitaciones adivinaste el numero {numero_aleatorio} correctamente !!!.")


adivina_el_numero(10)
