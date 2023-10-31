for n in range(1,200):
    n = bin(n)[2:]
    sum = n.count('1')
    ost = sum % 2
    if ost != 0:
        n += str('11')
    else:
        n += str('00')
    R = int(n,2)
    if R > 114:
        print(R)
        break