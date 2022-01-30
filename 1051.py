x = float(input())
if x >= 0 and x <= 2000:
    print("Isento")
elif x >= 2000.01 and x <= 3000:
    x = x-2000
    x = x*0.08
    print("R$ {0:.2f}".format(x))
elif x >= 3000.01 and x <= 4500:
    x = x-2000
    faixa1 = 1000*0.08
    x = x-1000
    x = x*0.18
    x = x+faixa1
    y = 0.18
    print("R$ {0:.2f}".format(x))
elif x > 4500:
    x = x-2000
    faixa1 = 1000*0.08
    x = x-1000
    faixa2 = 1500*0.18
    x = x-1500
    x = x*0.28
    x = x+faixa1+faixa2
    print("R$ {0:.2f}".format(x))
