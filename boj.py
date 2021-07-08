import sys
input = sys.stdin.readline


input_list = []
t = int(input())
for i in range(t):
    n = int(input().strip())
    temp = []
    for _ in range(n):
        temp.append(input().strip())


    temp.sort()

    for a,b in list(zip(temp, temp[1:])):
        print(a,b)
        if b.startswith(a):
            print("NO")
            break
    else: print("YES")

