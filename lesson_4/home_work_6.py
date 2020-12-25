from itertools import count, cycle

for el in count(int(input('Введите стартовое число '))):
    print(el, end='')
    quit = input()
    if quit == 'q':
        break

my_list = [True, 'ABC', 123, None]
iter = cycle(my_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()
    if quit == 'q':
        break


