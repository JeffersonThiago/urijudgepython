valor = 0
pos = 0
for i in range(100):
    x = int(input())
    if x > valor:
        valor = x
        pos = i+1
print(valor)
print(pos)
