x = int(input())
arr = list(map(int, input().split()))
min = arr[0]
max = arr[0]
for i in range(x):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]
print(min,max)