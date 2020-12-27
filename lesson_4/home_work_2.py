my_list = [12, 3, 4, 1, 7, 5, 4, 10]
my_new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
