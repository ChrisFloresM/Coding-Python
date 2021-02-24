#Christian Flores 14/02/2021

def mutate_string(string, position, character):
    string = list(string)
    del string[position]
    string.insert(position, character)
    string = "".join(string)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)