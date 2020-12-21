my_str = input("Ввести строку: ")
a = my_str.split(' ')
for ind, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(ind, el)