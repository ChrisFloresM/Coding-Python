#Christian Flores 14/02/2021

while True:
    print("\nEnter 'q' to quit")
    name = input("Enter your name: ")
    if name.lower() == "q":
        break
    with open("Chapter_10_Text_Exceptions/guest_book.txt", "a") as guest_book:
        guest_book.write(f"{name}\n")
    print("Your name has been succesfully registered")
    
    