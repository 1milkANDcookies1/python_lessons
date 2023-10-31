import math
# работа с текстом: 
name = "эля"
print(len(name)) # считает кол-во букв 
print(name.upper()) # все заглавные буквы
print(name.lower()) # все маленькие буквы
number = 4
print(str(number)) # превращает число в текст 
print(name.replace('э', 'ля')) # найди старое и замени на новое
print(name)
print(name.count('л')) # считает кол-во набранных букв 
# функции для работы с математикой 
print(bin(5)[2:]) # переводим в двоичную систему и убираем знаки, обозначающие систему 
print(int('1')) #переводим текст в целое число
print(type(1)) # узнаем тип данных
print(type('1')) 
print(float('1')) # превращаем в дробное число
print(int('A',16)) # переводим заданное число в заданной системе счисления в дисятичное 
print(math.pi) # достаем число пи из математической библиотеки
print(math.floor(7.9)) # округляем число в сторону "пола"
print(math.ceil(7.2)) # округляем число в сторону "потолка"
print(int(4.7)) # читает цифру до точки, выбрасывает остальное
print(round(5.589,2))
print(sum([6,7]))
print(4%2)
print(13//2)
print(2**3)
print(4**0.5)
print(math.sqrt(64))
print(pow(4,2))
#коллекция
text = 'apple orange milk'
print(text.split())