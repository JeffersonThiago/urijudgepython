lista = []
for i in range(5):
    v1 = int(input())
    teste = v1 % 2
    if teste == 0:
        lista.append(v1)

print(len(lista), "valores pares")
