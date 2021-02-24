#Christian Flores 12/02/2021
from messages_module import send_messages as se_me
from messages_module import show_messages as sh_me

messages = ["Hola, ¿que tal?", "Puedo ayudarte?", "Nunca digas nunca"]
sent_messages = []

se_me(messages[:], sent_messages)
sh_me(messages)
sh_me(sent_messages)

