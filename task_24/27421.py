with open('task_24.txt/24_demo.txt', 'r') as f:
    info = f.read()
    max_letters = 0
    current_number = 1
    for letter in range(1,len(info)):
        if info[letter] != info[letter - 1]:
            current_number += 1
        else:
            max_letters = max(max_letters,current_number)
            current_number = 1
max_letters = max(max_letters,current_number)
print(max_letters)