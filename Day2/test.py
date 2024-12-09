a = [1, 2, 3, 4, 5]

for x in range(len(a)):
    atest = a.copy()
    del atest[x]
    print(atest)