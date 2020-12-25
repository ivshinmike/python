time = int(input('Введите время в секундах: '))
h = ((time // 3600)) % 24
m = (time // 60) % 60
s = time % 60

print(f"{h:02} : {m:02} : {s:02}")

