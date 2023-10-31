for n in range(1,200):
    n = bin(n)[2:]
    sum = n.count('1')
    ost = sum % 2
    n += str(ost)

    sum = n.count('1')
    ost = sum % 2
    n += str(ost)
    R = int(n,2)
    if R > 83:
        print(R)
        break