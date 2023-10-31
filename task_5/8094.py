for n in range(1,100):
    num = bin(n)[2:]
    ost = num.count('1')%2 
    num = num + str(ost) 
    ost = num.count('1')%2 
    num = num + str(ost) 
    R = int(num,2)
    if R > 43:
     print(R)
     break