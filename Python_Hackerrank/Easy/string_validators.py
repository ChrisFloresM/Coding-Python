#Christian Flores

def check_for_alnum(string):
    for letter in string:
        if letter.isalnum():
            condition = True
            break
        else:
            condition = False
    print(condition)


def check_for_alpha(string):
    for letter in string:
        if letter.isalpha():
            condition = True
            break
        else:
            condition = False
    print(condition)


def check_for_digit(string):
    for letter in string:
        if letter.isdigit():
            condition = True
            break
        else:
            condition = False
    print(condition)


def check_for_lower(string):
    for letter in string:
        if letter.islower():
            condition = True
            break
        else:
            condition = False
    print(condition)


def check_for_upper(string):
    for letter in string:
        if letter.isupper():
            condition = True
            break
        else:
            condition = False
    print(condition)

if __name__ == '__main__':
    s = input()

check_for_alnum(s)
check_for_alpha(s)
check_for_digit(s)
check_for_lower(s)
check_for_upper(s)
