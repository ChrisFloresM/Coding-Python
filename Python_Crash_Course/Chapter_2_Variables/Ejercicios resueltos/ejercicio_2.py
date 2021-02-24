#Ejercicios de strings y metodos
name = "ada lovelace"
print(name.title())

#strings con variables
first_name = "chris"
last_name = "flores"
full_name = f"{first_name} {last_name}"
message = f"Hello {full_name.title()}!"
print(message)

#Recortar espacios en blanco
user_input = "python "
user_input_2 = " python"
print(user_input)
print(user_input.rstrip())
print(user_input_2)
print(user_input_2.lstrip())
print(user_input.strip())
print(user_input_2.strip())

