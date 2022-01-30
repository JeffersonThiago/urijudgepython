n = int(input())
array = []
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        soma = 0
        for i in range(y+1, x):
            if i % 2 == 1:
                soma += i
        array.append(soma)
    else:
        soma = 0
        for i in range(x+1, y):
            if i % 2 == 1:
                soma += i
        array.append(soma)

for i in array:
    print(i)
