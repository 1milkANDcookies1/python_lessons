for n in range(100,1000):
    n = str(n)
    new_n1 = int(n[0]) + int(n[1])
    new_n2 = int(n[1]) + int(n[2])
    if new_n1 > new_n2:
        result = str(new_n1) + str(new_n2)
    elif new_n1 < new_n2:
        result = str(new_n2) + str(new_n1) 
    else:
        result = str(new_n1) + str(new_n2)  
    if result == "1412":
        print(n)
        break
