arr = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    arr[i] = int(input())
for i in range(10):
    arr[i] = (arr[i] % 42)
list = set(arr)
print(len(list))
