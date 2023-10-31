file = open('data.txt', 'r')
print(file.read())
file.close() # опасный 

with open('data.txt', 'r') as f:
    info = f.read()
    print(info)
    for line in info:
        print(line)

with open('data.txt', 'r') as text:
    info = text.readlines()
    print(info)
    for line in info:
        print(line.split(','), end = '')