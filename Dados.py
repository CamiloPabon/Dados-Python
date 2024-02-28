import random

decision = str
dados = int

while decision !="no":
    print("Desea dejar de lanzar el dado?")
    decision = input()
    if decision == "si":
        print("Lanzando el dado...")
        dados = random.randrange(1,7,1)
        print("El resultado del dado es: ",dados)
        
    else:
        print("Fin del programa")
        break
    