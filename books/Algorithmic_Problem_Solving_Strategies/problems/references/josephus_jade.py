def func(N, k):
    A = range(1, N+1)
    i = 0
    while len(A)>2:
        while i>=len(A):
            i = i - len(A)
        A.pop(i)
        i += k-1
    return A

c = int(raw_input())

case = []

for i in range(c):
    p = raw_input()
    case.append(p)
    
for i in range(c):
    print func(int(case[i].split(' ')[0]), int(case[i].split(' ')[1]))[0], func(int(case[i].split(' ')[0]), int(case[i].split(' ')[1]))[1]