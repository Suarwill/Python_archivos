def Fibo(sec):
    n = nn = 1
    for x in range(sec):
        if x in [0, 1]:
            yield 1
        else:
            new = n + nn
            nn, n = n, new
            yield new

User_Op = int(input("Eliga cantidad de numero/s en secuencia Fibonnaci a mostrar: "))
fib_sec = list(Fibo(User_Op))
print(fib_sec[-1])