#Christian Flores 16/02/2021

from math import ceil

n, m = map(int, input().split())
pattern = [(".|."*i).center(m,"-") for i in range(1, n, 2)]
welcome_message = "welcome".center(m,"-") + "\n"
print("\n".join(pattern) + "\n" + welcome_message.upper() + "\n".join(pattern[::-1]))