def user_inf(name, surname, birthday, city, email, phone):
    return(name, surname, birthday, city, email, phone)

print(user_inf(name=input('Ввести ваше имя: '), surname=input('Ввести вашу фамилию: '), birthday=int(input('Дата рождения: ')),
      city=input('Город проживания: '), email=input('email: '), phone=int(input('Телефон: '))))