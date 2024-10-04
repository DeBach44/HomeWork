#DeBach
while True:
    a = int(input("Введите число: "))
    l = []
    for i in range(1,21):
        if i >= a:
            break
        else:
            for j in range(i+1,21):
                if a % (i + j) == 0:
                    l.append(i)
                    l.append(j)
                elif(i + j) >= a:
                    break
                else:
                    continue
    print(f"{a}: {l}")