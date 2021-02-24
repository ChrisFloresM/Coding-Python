#Christian Flores 11/02/2021
#Uso de comandos con listas
list = []
commands = []
if __name__ == '__main__':
    N = int(input())
for _ in range(N):
    full_command = input()
    command = full_command.split()
    commands.append(command)

for command in commands:
    if command[0].lower() == "insert":
        list.insert(int(command[1]), int(command[2]))
    elif command[0].lower() == "print":
        print(list)
    elif command[0].lower() == "remove":
        list.remove(int(command[1]))
    elif command[0].lower() == "append":
        list.append(int(command[1]))
    elif command[0].lower() == "sort":
        list.sort()
    elif command[0].lower() == "pop":
        list.pop()
    elif command[0].lower() == "reverse":
        list.reverse()




