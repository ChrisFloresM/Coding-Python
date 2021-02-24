#Christian Flores 20/02/2021

if __name__ == '__main__':
    arr = []
    sums = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            hourglass = [element[j:j+3] for element in arr[i:i+3]]
            sums.append(sum(list(map(sum, hourglass[:3:2]))) + hourglass[1][1])
            
    print(max(sums))
