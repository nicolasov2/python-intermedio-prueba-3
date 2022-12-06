import random

def piedra_papel_tijera():
    while True:
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
            break
        else:
            print("Ingrese una opcion valida")
    return opcion

def main():
    ganadas = 0;
    empate = 0;
    perdidas = 0;
    print("Bienvenido al juego de piedra, papel o tijera")
    print("1: Piedra 🪨")
    print("2: Papel ▭ ")
    print("3: Tijera ✁")
    print("4: Salir ->")
    while True:
        opcion = piedra_papel_tijera()
        if opcion == 4:
            print("ganaste: ", ganadas)
            print("perdiste", perdidas)
            print("empatados: ", empate)
            print("\nGracias por jugar :) tenga buena tarde")

            break
        else:
            
            opcion_computadora = random.randint(1,3)
            if opcion == 1 or opcion == 2 or opcion == 3:
                if opcion_computadora == 1:
                    print("La computadora eligio piedra")
                    print("-----------------------------")
                    print("[Empate :/]")
                    print("-----------------------------\n")
                    empate += 1
                elif opcion_computadora == 2:
                    print("La computadora eligio papel")
                    print("-----------------------------")
                    print("[Perdiste :()]")
                    print("-----------------------------\n")
                    perdidas += 1
                else:
                    print("La computadora eligio tijera")
                    print("-----------------------------")
                    print("[Ganaste :)]")
                    print("-----------------------------\n")
                    ganadas += 1
                    
            
if __name__ == '__main__':
    main()  
