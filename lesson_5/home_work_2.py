my_list = ['Hello world\n', 'Chao Nik\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += line.count("\n")
        words = len(line.split())
        print(f"{words} words in line")
    print(f"String count is {lines}")