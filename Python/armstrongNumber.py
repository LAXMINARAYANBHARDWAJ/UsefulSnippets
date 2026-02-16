a = int(input("Enter the range: "))

for i in range(0, a+1, 1):
    l = int(len(str(i)))
    summ = 0
    b = i
    while i != 0:
        summ = summ + ((i % 10) ** (l))
        i //= 10
    if summ == b:
        print(b)
    else:
        continue
