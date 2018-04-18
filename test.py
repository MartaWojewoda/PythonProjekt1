import math
#Która pizza jest wieksza
r1=int(input("Podaj promien pierwszej pizzy: "))
r2=int(input("Podaj promien drugiej pizzy: "))
pizza1=r1*math.pi**2
pizza2=r2*math.pi**2

if pizza1<pizza2:
    print("pizza 1 jest mniejsza")
else:
    print("pizza 2 jest mniejsza")