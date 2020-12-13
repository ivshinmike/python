first = float(input('начальный результат в км '))
next = float(input('ожидаемый результат в км '))
result = first * 0.1
days = 1
while first < next:
    first += first * 0.1
    days += 1

print(f'Спортсмен достигнет ожидаемого результата за {days} дней')
