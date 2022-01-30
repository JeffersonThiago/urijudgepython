x = int(input())
inside = 0
outside = 0
for i in range(x):
    y = int(input())
    if y >= 10 and y <= 20:
        inside += 1
    else:
        outside += 1
print(inside, "in")
print(outside, "out")
