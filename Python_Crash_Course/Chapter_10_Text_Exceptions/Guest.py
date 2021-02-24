#Christian Flores 14/02/2021


name = input("Please, input your name: ")
with open("Chapter_10_Text_Exceptions/guest.txt", "w") as name_file:
    name_file.write(name)

    