my_list = [7, 1, 4, 4, 2, 3, 7, 2, 8, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)