with open('task_24.txt/24.1_demo.txt', 'r') as f:
    info = f.read()
    max_letters = 0
    current_number = 1
    for letter in range(1,len(info)):
        if info[letter] == 'X' and info[letter - 1] == 'X':
            current_number += 1
        else:
            max_letters = max(max_letters,current_number)
            current_number = 1
max_letters = max(max_letters,current_number)
print(max_letters)    # 19

print(len('XXXXXXXXXXXXXXXXXXX'))