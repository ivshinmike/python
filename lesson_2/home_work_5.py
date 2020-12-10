new_el = int(input("Ввести новый элемент рейтинга: "))
rating = [7, 4, 3, 2]
i = 0
for element in rating:
    if new_el <= element:
        i += 1
rating.insert(i, new_el)
print(rating)