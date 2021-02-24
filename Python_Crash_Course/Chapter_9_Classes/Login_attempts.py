#Christian Flores 13/02/2021

class Users:

    #Este es el método constructor
    def __init__(self, first_name, last_name, age):
        """Inicializar atributos del usuario"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loggin_attempts = 0

    def describe_user(self):
        """Metodo que despliega la informacion del usuario"""
        print("\nUser information: ")
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"age: {self.age}")

    def greet_user(self):
        """Mostrar un saludo al usuario"""
        print(f"Hi {self.first_name} {self.last_name}, have a good day today!")

    def increment_loggin_attempts(self):
        """Incrementar los intentos de loggin en 1"""
        self.loggin_attempts += 1

    def reset_loggin_attempts(self):
        """Metodo que reinicia los intentos de loggin a 0"""
        self.loggin_attempts = 0

new_user = Users("Christian", "Flores", 22)

new_user.increment_loggin_attempts()
new_user.increment_loggin_attempts()
new_user.increment_loggin_attempts()

print(f"You have tried to login {new_user.loggin_attempts} times. Please, stop it...")
new_user.reset_loggin_attempts()

print(f"Your loggin attempts has been restored to {new_user.loggin_attempts}")

    