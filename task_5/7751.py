for n in range (1001,10000):
    n = str(n)
    new_n1 = int(n[0]) + int(n[1])
    new_n2 = int(n[2]) + int(n[3])
    if new_n1 > new_n2:
        R = str(new_n2) + str(new_n1) # можно ли запиать int(R) = ... или R = int(str(new_n2) + str(new_n1))
    elif new_n2 > new_n1:
        R = str(new_n1) + str(new_n2)
        if R == '117':
            print(n) # 7092

'''for i in range(10000, 1000, -1):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[2]) + int(s[3])
    first = str(min(k1, k2))
    second = str((max(k1, k2)))
    s1 = first + second
    if s1 == '117':
        print(i)
        break'''
        