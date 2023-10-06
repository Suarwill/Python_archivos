import random, os, time

def Welcome         ():             # Mensaje de Bienvenida
    print ("\n"+"="*40,"\nBienvenido\n\nEste es un Juego sencillo\nde Piedra, Papel o Tijera\n"+"-"*30)
    print ("Jugará contra la CPU\n\nSuerte !\n"+"="*40+"\n")
    time.sleep(3) ; os.system("cls")

    return

def Despedida       (Fin):          # Mensaje Final y Estadisticas
    os.system("cls")
    print                       ("\n"+"="*40)
    print ("Fin del Juego\nHa ganado   ", Fin[0],"partidas",
           "\nHa perdido  ",              Fin[1],"partidas",
           "\nHa empatado ",              Fin[2],"partidas")
    print ("-"*30+"\nHasta la próxima\n"+"="*40+"\n")
    time.sleep(3)
    while True:     Exit = input("")    ;   break
    return

def SeleccionUser   ():             # Seleccion Papel/Piedra/Tijera
    while True:
        Op_User = input("\nPiedra  (z)\nPapel   (x)\nTijera  (c)\n\nTerminar Juego  (s)\n\nElija su opcion : ")
        if Op_User == "z":      Op_User = "Piedra"  ;   break
        elif Op_User == "x":    Op_User = "Papel"   ;   break
        elif Op_User == "c":    Op_User = "Tijera"  ;   break
        elif Op_User == "s":                            break
        else:                   print ("x"*40+"\nSeleccione una opcion válida\n"+"x"*40)
    os.system("cls")
    return Op_User

def InterfaseCPU    ():             # Mensaje de carga animado, "CPU Esta Eligiendo"
    os.system("cls")
    msj = "\nLa CPU esta pensando."
    for tp in range (3):
        print (msj+"."*tp)
        time.sleep(1)
        os.system("cls") 
    return

def ResultadoVS     (msj,Op_User,Op_CPU):
    print ("\n"+msj+"\n")
    print ("Elegiste",Op_User,"y la CPU eligio",Op_CPU)
    return

def Juego():
    __Start__ = Welcome()
    Opciones = ["Piedra","Papel","Tijera"]
    Contador, Win, Lose, Draw = 1,0,0,0
    while True:
        print                   ("\n"+"="*40)
        print ("Partida N° ",Contador)
        print                   ("="*40)
        Op_CPU, Op_User = random.choice(Opciones), SeleccionUser()
        print                   ("-"*30)

        if (Op_User == "Tijera" and Op_CPU == "Papel") or (Op_User == "Papel" and Op_CPU == "Piedra") or (Op_User == "Piedra" and Op_CPU == "Tijera"):
            InterfaseCPU()
            msj = ResultadoVS("Ganaste !!!",Op_User,Op_CPU)
            Win += 1
        elif (Op_User == "Tijera" and Op_CPU == "Piedra") or (Op_User == "Papel" and Op_CPU == "Tijera") or (Op_User == "Piedra" and Op_CPU == "Papel"):
            InterfaseCPU()
            msj = ResultadoVS("Perdiste !!!",Op_User,Op_CPU)
            Lose += 1
        elif Op_User == "s":
            print ("\n\n\nFinalizando e imprimiendo estadísticas\n\n\n")
            break
        else:
            InterfaseCPU()
            msj = ResultadoVS("Empate !!!",Op_User,Op_CPU)
            Draw += 1
        print                   ("-"*30)
        Contador += 1
        time.sleep(3)   ;   os.system("cls")
    return [Win,Lose,Draw]

__Main__  = Juego()
__End__   = Despedida(__Main__)
