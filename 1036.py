import math

a, b, c = map(float, input().split())


d = (2*a)
try:
    raiz = math.sqrt((b**2)-4*a*c)
    if d == 0:
        print("Impossivel calcular")

    else:
        x1 = (-b+raiz)/d
        x2 = (-b-raiz)/d
        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
except:
    print("Impossivel calcular")
