# Numera del 1 al 100, si es divisible por 3 imprime Fizz, si es divisible por 5 imprime Buzz
# Si es divisible por 3 y 5, imprime FizzBuzz
# Nivel mas dificil, no uses operador de residuo %

import time

#                       Nivel sin usar el Operador %
Mult3, Mult5, Mult15 = [],[],[]                         # Para evitar el uso de operador %, usaremos listas con los números multiplos y compararlos.
for multiplo in range(34):
    mult = 3 * multiplo
    Mult3.append(mult)
for multiplo in range(21):
    mult = 5 * multiplo
    Mult5.append(mult)
for multiplo in range(7):
    mult = 15 * multiplo
    Mult15.append(mult)     

for num in range (1,100):
    if num in list(Mult15):     print ("FizzBuzz")      # Si el Numero es múltiplo de 3 y 5, imprimira FizzBuzz.
    elif num in (Mult3):        print ("Fizz")          # Si el Numero es múltiplo de 3, imprimira Fizz.
    elif num in (Mult5):        print ("Buzz")          # Si el Numero es múltiplo de 5, imprimira Buzz.
    else:                       print (num)             # Cualquier otro numero se imprimira normalmente.


#                       Nivel usando el Operador %
for num in range (1,100):
    if  num % 15 == 0   :       print ("FizzBuzz")      # Si el Numero es múltiplo de 3 y 5, imprimira FizzBuzz.
    elif num % 3 == 0   :       print ("Fizz")          # Si el Numero es múltiplo de 3, imprimira Fizz.
    elif num % 5 == 0   :       print ("Buzz")          # Si el Numero es múltiplo de 5, imprimira Buzz.
    else:                       print (num)             # Cualquier otro numero se imprimira normalmente.

time.sleep(10)