def calc_hipotenusa():
    Cat_A =     int(input("Ingrese la medida del Cateto A (metros) : "))
    Cat_B =     int(input("Ingrese la medida del Cateto B (metros) : "))
    Hipo =      (Cat_A**2+Cat_B**2)**0.5
    return print("\nLa medida de la Hipotenusa es de : ",Hipo,"metros\n")
def calc_cateto():
    Cat_A =     int(input("Ingrese la medida del Cateto A (metros) : "))
    Hipo =      int(input("Ingrese la medida de la Hipotenusa (metros) : "))
    Cat =       (Hipo**2-Cat_A**2)**0.5
    return print("\nLa medida del Cateto es de : ",Cat,"metros\n")
def Calculadora_Teorema():
    print ("- "*20+"\nBienvenido a esta calculadora para \nEl TEOREMA de PITAGORAS\n"+"- "*20)
    Op_User = int(input("¿Que dato quiere calcular? : \n\n(1) Hipotenusa\n(2) Cateto \n\nSeleccione opcion: "))
    while True:
        if Op_User == 1:        
            calc_hipotenusa()
            break
        elif Op_User == 2:      
            calc_cateto()
            break
        else:                   
            print("Favor elija una opcion válida")
    return input("- "*20+"\nGracias por utilizar esta calculadora\n"+"- "*20)

__main__ = Calculadora_Teorema()