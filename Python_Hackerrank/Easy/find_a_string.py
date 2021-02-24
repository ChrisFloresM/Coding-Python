#Christian Flores 14/02/2021

#Codigo que encuentra un fragmento (substring) en un string y cuenta cuantas veces aparece
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)+1-len(sub_string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)