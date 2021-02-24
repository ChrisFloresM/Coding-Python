#Christian Flores 15/02/2021

count = 0
print("Enter 'q' to exit")
while True:
    num = input("Enter a number: ")
    if num == "q":
        break
    try:
        num = int(num)
    except ValueError:
        pass
    else:
        count += num
print(f"The sum is {count}")
    

