n = int(input())
array = []
for i in range(n):
    a, b, c = map(float, input().split())
    media = ((a*2)+(b*3)+(c*5))/10
    array.append(media)

for i in array:
    print("{0:.1f}".format(i))
