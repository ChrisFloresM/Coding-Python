#Christian Flores 17/02/2021

n = int(input())
phones_book = {}
for _ in range(n):
    name, phone = input().split()
    phones_book[name] = phone

while True:
    try:
        name_to_search = input()
        if name_to_search in phones_book.keys():
            print(f"{name_to_search}={phones_book[name_to_search]}")
        else:
            print("Not found")
    except EOFError:
        break
    
    



