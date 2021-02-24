#Christian Flores 18/02/2021

def minion_game(string):
    # your code goes here
    vowels = ["a","e","i","o","u"]
    stuart_score = 0
    kevin_score = 0
    for i in range(len(string)):
        if string[i].lower() in vowels:
            kevin_score += (len(string)-i) 
        else:
            stuart_score += (len(string)-i)
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print(f"Draw")

        

if __name__ == '__main__':
    s = input()
    minion_game(s)