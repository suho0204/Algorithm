n = int(input())
arr = set()

for _ in range(n):
    arr.add(input())

arr = sorted(arr, key=lambda x: (len(x), x))

for word in arr:
    print(word)