#Christian Flores 17/02/2021

size = 5
number = 96+size
width = 4*size-3
elements = []

for i in range(number-1, 95, -1):
    initial_pat = [chr(alpha) for alpha in range(number, i, -1)]
    final_pat = initial_pat[::-1]
    string = "-".join(initial_pat + final_pat[1:]).center(width,"-")
    elements.append(string)

print("\n".join(elements)+"\n"+"\n".join(elements[::-1][1:]))
    
    

