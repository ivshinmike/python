def sum_num():
    result = 0
    while True:
        line = input("Enter number or special sign q to exite: ").split()
        for number in line:
            if number == 'q':
                return result
            else:
                try:
                    result += int(number)
                except ValueError:
                    print("To exit the program, enter - 'q'.")
        print(f"You sum is {result}.")

print(sum_num())


