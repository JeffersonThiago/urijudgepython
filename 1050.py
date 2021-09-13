x = int(input())
ddd = [61, 71, 11, 21, 32, 19, 27, 31]
destination = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro",
               "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

for i in range(9):
    try:
        if x == ddd[i]:
            print(destination[i])
            break
    except:
        print("DDD nao cadastrado")
