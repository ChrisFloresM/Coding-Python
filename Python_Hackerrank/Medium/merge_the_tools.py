#Christian Flores 18/02/2021

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        substring = string[i:i+k]
        new_string = []
        for letter in substring:
            if letter not in new_string:
                new_string.append(letter)
        final_string = "".join(new_string)
        print(final_string)

# your code goes here
#while string:
#    s = string[0:k]
#    seen = ''
#    for c in s:
#        if c not in seen:
#            seen += c
#    print(seen)
#    string = string[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)