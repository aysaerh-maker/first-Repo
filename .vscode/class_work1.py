number = int(input("enter the number here: "))
for i in range(1, number +1):
    if i % 2 != 0:
        continue
    else:
        print(i)