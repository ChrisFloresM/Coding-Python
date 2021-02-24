#Christian Flores 12/02/2021
def send_messages(messages, sent_messages):
    """Funcion que simula el mandar los mensajes"""
    print("\n")
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
    sent_messages.reverse()

def show_messages(messages):
    """Funcion que imprime mensajes"""
    print("\n")
    print(messages)