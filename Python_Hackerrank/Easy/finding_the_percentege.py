#Christian Flores 14/02/2021

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_marks = student_marks[query_name]
    sum = 0
    for mark in query_marks:
        sum += mark
    print("{:.2f}".format(sum/3))