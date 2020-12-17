number_us = int(input('Введите целое положительное число: '))
max = number_us % 10
number = number_us // 10
while number > 0:
    if number % 10 > max:
        max = number % 10
    number = number // 10
print(f'самая большая цифра в числе {number_us} равна {max}')
