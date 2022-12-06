import random

def adivinar_numero():
    numero = random.randint(1,100)
    intentos = 0
    while intentos < 10:
        intentos += 1
        print("Intento numero: ", intentos)
        print("Adivina el numero: ")
        adivina = int(input())
        if adivina < numero:
            print("El numero es mas grande")
        elif adivina > numero:
            print("El numero es mas pequeño")
        else:
            break
        
    if adivina == numero:
        print("Muy bien! Adivinaste el numero en ", intentos, " intentos")
    else:
        print("intentos acabados, el numero era ", numero)

def main():
    print("jugaremos a adivinar un numero")
    print("el numero esta entre 1 y 100")
    print("tienes 10 intentos")
    print("buena suerte :)")
    while True:
        adivinar_numero()
        break
    print("Gracias por jugar")


if __name__ == '__main__':
    main()
