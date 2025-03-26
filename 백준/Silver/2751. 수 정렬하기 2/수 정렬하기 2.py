import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline())
    arr.append(x)
arr.sort()
for i in range(len(arr)):
    print(arr[i])