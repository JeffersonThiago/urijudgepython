x = int(input())
y = int(input())

z = 0
if x < y:
    for i in range(x+1, y):
        if i % 2 == 1:
            z = z+i
    print(z)
else:
    for i in range(y+1, x):
        if i % 2 == 1:
            z = z+i
    print(z)
