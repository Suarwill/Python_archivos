"""El concursante debe elegir una puerta entre tres (todas cerradas).
el premio consiste en llevarse lo que se encuentra detrás de la elegida. 
Se sabe con certeza que tras una de ellas se oculta un automóvil, y tras las otras dos hay cabras. 
Una vez que el concursante haya elegido una puerta y comunicado su elección a los presentes, 
el presentador, que sabe lo que hay detrás de cada puerta, abrirá una de las otras dos, 
en la que habrá una cabra. 
A continuación, le da la opción al concursante de cambiar, si lo desea, 
de puerta (tiene dos opciones). 
¿Debe el concursante mantener su elección original o escoger la otra puerta? 
¿Hay alguna diferencia?
Cuales son los porcentajes de acierto, al cambiar/permanecer en la misma puerta, realiza ejemplo."""

import random

def azar ():
    GANADORA = random.choice(("A","B","C"))
    if GANADORA == "A":
        PERDEDORA1,PERDEDORA2 = "B","C"
    elif GANADORA == "B":
        PERDEDORA1,PERDEDORA2 = "A","C"
    else:
        PERDEDORA1,PERDEDORA2 = "A","B"
    return (GANADORA,PERDEDORA1,PERDEDORA2)

def concursoPausado():
    GANADORA,PERDEDORA1,PERDEDORA2 = azar()
    NOGANADORAS = (PERDEDORA1,PERDEDORA2)
    while True:
        CONCURSANTE = str.upper(input("Elige una puerta (A, B o C): "))
        print ("Elegiste la puerta : ",CONCURSANTE)
        if CONCURSANTE == GANADORA:
            ABIERTA = random.choice((NOGANADORAS))
            if ABIERTA == PERDEDORA1:   NOABIERTA = PERDEDORA2
            else:                       NOABIERTA = PERDEDORA1
            print ("En la puerta ",ABIERTA,"hay una CABRA")
            break
        elif CONCURSANTE == PERDEDORA1:
            ABIERTA,NOABIERTA = PERDEDORA2,PERDEDORA1
            print ("En la puerta ",ABIERTA,"hay una CABRA")
            break
        elif CONCURSANTE == PERDEDORA2:
            ABIERTA,NOABIERTA = PERDEDORA1, PERDEDORA2
            print ("En la puerta ",ABIERTA,"hay una CABRA")
            break
        else:
            print ("Por favor eliga una puerta correctamente")

    NUEVADECISION = str.upper(input("¿Quiere cambiar de PUERTA? ( SI / NO ) : "))

    if NUEVADECISION == "SI" and CONCURSANTE == GANADORA:
        print ("\nLo lamentamos, has perdido el AUTO se encontraba en la PUERTA ", GANADORA)
    elif NUEVADECISION == "NO" and CONCURSANTE == NOABIERTA:
        print ("\nLo lamentamos, has perdido el AUTO se encontraba en la PUERTA ", GANADORA)
    else:
        print ("\nFelicitaciones, has ganado un AUTO, la puerta correcta era la : ", GANADORA)
    return

def concursoPausado(Cant_Sorteos,):
    GANADORA,PERDEDORA1,PERDEDORA2 = azar()
    Cant_Sorteos = ()
    NOGANADORAS = (PERDEDORA1,PERDEDORA2)
    while True:
        CONCURSANTE = str.upper(input("Elige una puerta (A, B o C): "))
        print ("Elegiste la puerta : ",CONCURSANTE)
        if CONCURSANTE == GANADORA:
            ABIERTA = random.choice((NOGANADORAS))
            if ABIERTA == PERDEDORA1:   NOABIERTA = PERDEDORA2
            else:                       NOABIERTA = PERDEDORA1
            print ("En la puerta ",ABIERTA,"hay una CABRA")
            break
        elif CONCURSANTE == PERDEDORA1:
            ABIERTA,NOABIERTA = PERDEDORA2,PERDEDORA1
            print ("En la puerta ",ABIERTA,"hay una CABRA")
            break
        elif CONCURSANTE == PERDEDORA2:
            ABIERTA,NOABIERTA = PERDEDORA1, PERDEDORA2
            print ("En la puerta ",ABIERTA,"hay una CABRA")
            break
        else:
            print ("Por favor eliga una puerta correctamente")

    NUEVADECISION = str.upper(input("¿Quiere cambiar de PUERTA? ( SI / NO ) : "))

    if NUEVADECISION == "SI" and CONCURSANTE == GANADORA:
        print ("\nLo lamentamos, has perdido el AUTO se encontraba en la PUERTA ", GANADORA)
    elif NUEVADECISION == "NO" and CONCURSANTE == NOABIERTA:
        print ("\nLo lamentamos, has perdido el AUTO se encontraba en la PUERTA ", GANADORA)
    else:
        print ("\nFelicitaciones, has ganado un AUTO, la puerta correcta era la : ", GANADORA)
    return

__main__= concursoPausado()