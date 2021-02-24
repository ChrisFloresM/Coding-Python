#Christian Flores 14/02/2021

with open('Chapter_10_Text_Exceptions/file_1.txt') as my_file:
    contents = my_file.readlines()

for line in contents:
    new_line = line.replace("Python", "Javascript")
    print(new_line.strip())


