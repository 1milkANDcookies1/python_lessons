n = int(input())
result = bin(n)[2:]
sum = result.count('1')
ost = sum % 2
result = str(result) + str(ost)

sum = result.count('1')
ost = sum % 2
result = str(result) + str(ost)

print(int(result))
    