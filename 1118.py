op = 1
while True:
    if op == 1:
        nota1 = float(input())
        while nota1 < 0 or nota1 > 10:
            print("nota invalida")
            nota1 = float(input())
        nota2 = float(input())
        while nota2 < 0 or nota2 > 10:
            print("nota invalida")
            nota2 = float(input())
        media = (nota1+nota2)/2
        print("media = {0:.2f}".format(media))
    elif op == 2:
        break
    print("novo calculo (1-sim 2-nao)")
    op = int(input())
