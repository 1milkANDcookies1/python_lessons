with open('task_24.txt/24_33101.txt','r') as f:
    info = f.readlines()
    counter = 0
    for line in info:
    if line.count('A') > line.count('E'):
        counter += 1
print(counter)