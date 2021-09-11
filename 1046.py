a, b = map(int, input().split())

if b == a:
    print("O JOGO DUROU 24 HORA(S)")
elif b > a:
    h = b-a
    print("O JOGO DUROU %d HORA(S)" % h)
elif b < a:
    h = (24-a) + b
    print("O JOGO DUROU %d HORA(S)" % h)
