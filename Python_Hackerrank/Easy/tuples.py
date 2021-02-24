#Christian Flores 11/02/2021


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

list = [number for number in integer_list]
t = tuple(list)
new_t = (1, 2)
print(hash(new_t))