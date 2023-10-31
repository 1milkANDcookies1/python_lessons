for n in range(1000,10000):
    n = str(n)
    new_n1 = int(n[0])*int(n[1])
    new_n2 = int(n[2])*int(n[3])
    if new_n1 >= new_n2:
        R = str(new_n1) + str(new_n2)
    if new_n1 <= new_n2:
        R = str(new_n2) + str(new_n1)
    if int(R) == 124:
        print(n)
        break