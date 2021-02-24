#Christian Flores  10/02/2021
users = ["Andy", "Luis", "Admin", "Carlos", "Maria"]
lower_users = []
if users:
    for user in users:
        if user == "Admin":
            print("Hello Admin! Would you check the status of the site?")
        else:
            print(f"Hello {user}, welcome again")
        lower_users.append(user.lower())
else:
    print("We need to find more users")

new_users = ["Adrian", "luis", "roberto", "karla"]
print("\n")
for user in new_users:
    if user in lower_users:
        print(f"Sorry, but {user} is already taken. Try with a different name")
    else:
        print(f"Your username {user} has been successfully registred!")

