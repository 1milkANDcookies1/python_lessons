for n in range(100,1000):
    n = str(n)
    new_n1 = int(n[0]) + int(n[1])
    new_n2 = int(n[1]) + int(n[2])
    if new_n1 >= new_n2:
        R = str(new_n2) + str(new_n1)
    elif new_n2 >= new_n1:
        R = str(new_n1) + str(new_n2)
    if int(R) == 1115:
        print(n)
        break
