import math

a, b, c = map(float, input().split())
lista = [a, b, c]
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2+c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > (b**2+c**2):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2+c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a) or (b == a and b != c) or (c == b and c != a) or (c == a and c != b):
        print("TRIANGULO ISOSCELES")
