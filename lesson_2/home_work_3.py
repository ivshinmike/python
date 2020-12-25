month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
list = ['winter', 'spring', 'summer', 'autumn']
dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 1 or month == 12 or month == 2:
        print(dict.get(1))
        print(list[0])
elif month == 3 or month == 4 or month == 5:
    print(dict.get(2))
    print(list[1])
elif month == 6 or month == 7 or month == 8:
    print(dict.get(3))
    print(list[2])

elif month == 9 or month == 10 or month == 11:
    print(dict.get(4))
    print(list[3])