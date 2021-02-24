#Christian Flores 18/02/2021
#Dia 9: Recursion
#Calculando el factorial

def factorial(n):
    if n == 1:
        fact = 1
    else:
        fact = n*factorial(n-1)
    return fact
        
if __name__ == '__main__':
    n = int(input())
    print(factorial(n))


