'''with open('task_24.txt/24_27694.txt','r') as f:
    info = f.read()                          #прочитать файл
    counter = 0
    max_count = 0
    for letter in range(len(info)):
        if (info[letter] in 'AB') and (info[letter] != info[letter + 1]):
            counter += 1
            max_count = max(max_count,counter)
        else:
            counter = 0
max_count = max(max_count,counter)
print(max_count)'''

with open('task_24.txt/24_27694.txt','r') as f:
    info = f.read()
    counter = 0
    max_count = 0
    info = info.replace('AB','*')
    for letter in range(len(info)):
        if info[letter] == '*':
            counter += 1
            max_count = max(max_count,counter)
        else:
            counter = 0
max_count = max(max_count,counter)
print(max_count * 2)

print(len('ABABABABABABABABABABABAB'))