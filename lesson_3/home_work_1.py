def func(x, y):
    try:
        x = int(x)
        y = int(y)
        rez = x / y
        return rez
    except ValueError:
        return "Enter only number"
    except ZeroDivisionError:
        return "y is'n be zero"

print(func(input("Enter x = "), input("Enter y = ")))