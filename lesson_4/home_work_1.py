from sys import argv

def salary():
    try:
        time, pay, bonus = map(float, argv[1:])
        #res = time * pay + bonus
        print(f'заработная плата сотрудника: {time * pay + bonus}')
    except ValueError:
        print('Ввести все три числа')

salary()