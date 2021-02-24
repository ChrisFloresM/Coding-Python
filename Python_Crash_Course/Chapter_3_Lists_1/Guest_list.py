#Invitaciones a cenar usando listas
guests_list = ["Carlos", "Larry", "Luis"]
message_1 = f"Hi, {guests_list[0]}, I'm a huge fan of your work and I'd like to invite you to a dinner"
message_2 = f"{guests_list[1]}, I think you're an amazing engineer and I'd like to invite you some pizza"
print(message_1)
print(message_2)

#Elimino a Luis de la lista de invitados porque estará ocupado peleando contra Godzilla
removed_guest = guests_list.pop()
print(f"{removed_guest} can't make it to the dinner")

#Agrego a Maria al lugar de Luis
guests_list.append("Maria")
message_3 = f"Hi, {guests_list[2]}, I'm a huge fan of your work and I'd like to invite you to a dinner"
print(message_3)
print("\nHey everyone, I just found a bigger table!\n")

#Coloco a Miguel en la posición 0
guests_list.insert(0, "Miguel")

#Coloco a Chris en la posición 2
guests_list.insert(2, "Chris")

#Coloco a Rosa en la posición 5
guests_list.append("Rosa")
message_4 = f"Hi, {guests_list[2]}, I'm a huge fan of your work and I'd like to invite you to a dinner"
message_5 = f"Hi, {guests_list[5]}, I'm a huge fan of your work and I'd like to invite you to a dinner"
message_6 = message_1 = f"Hi, {guests_list[0]}, I'm a huge fan of your work and I'd like to invite you to a dinner"
print(message_4)
print(message_5)
print(message_6)
print("\nI'm sorry, but I'd only can invite two persons\n")
deleted_1 = guests_list.pop(0)
deleted_2 = guests_list.pop(1)
deleted_3 = guests_list.pop(1)
deleted_4 = guests_list.pop(2)
print(f"I'm sorry {deleted_1}")
print(f"I'm sorry {deleted_2}")
print(f"I'm sorry {deleted_3}")
print(f"I'm sorry {deleted_4}")
print("\n")
print(f"Hi {guests_list[0]}, I'm happy to tell you that you're still invited")
print(f"Hi {guests_list[1]}, I'm happy to tell you that you're still invited")
del guests_list[0]
del guests_list[0]
print(guests_list)

