a, b, c, d = map(int, input().split())

if c == a:
    if d == b:
        h = 24
        minu = 0
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")
    elif d > b:
        h = 0
        minu = d-b
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")
    elif b > d:
        h = 23
        minu = b-d
        minu = 60-minu
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")

elif c > a:
    h = c-a
    if d == b:
        minu = 0
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")
    elif d > b:
        minu = d-b
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")

    elif b > d:
        h = h-1
        minu = b-d
        minu = 60-minu
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")

elif c < a:
    h = (24-a) + c
    if d == b:
        minu = 0
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")
    elif d > b:
        minu = d-b
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")

    elif b > d:
        h = h-1
        minu = b-d
        minu = 60-minu
        print("O JOGO DUROU", h, "HORA(S) E", minu, "MINUTO(S)")
