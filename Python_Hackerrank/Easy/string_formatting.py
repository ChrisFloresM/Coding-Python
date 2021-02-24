#Christian Flores 16/02/2020

def print_formatted(number):
    # your code goes here
    width = len(str(bin(number))[2:])
    for i in range(1, n+1):
        stri = str(i).rjust(width)
        stroct = str(oct(i))[2:].rjust(width)
        strhex = str(hex(i))[2:].rjust(width)
        strbin = str(bin(i))[2:].rjust(width)
        print(f"{stri} {stroct} {strhex.upper()} {strbin}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)