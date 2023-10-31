for n in range(1,150):
    result = n
    n = bin(n)[2:]
    sum = n.count("1")
    ost = sum % 2
    n = n + str(ost)

    sum = n.count("1")
    ost = sum % 2
    n = n + str(ost)
    R = int(n,2)
    if R>77:
        print(result)
        break