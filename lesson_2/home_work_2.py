my_list = []
n = int(input('Введите количество элементов: '))
for i in range(0, n):
    element = int(input())
    my_list.append(element)
print(f'{my_list}')
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2

print(my_list)
