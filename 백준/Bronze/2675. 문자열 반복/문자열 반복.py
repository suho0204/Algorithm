x = int(input())
for i in range(x):
    arr = input()
    num = int(arr[0])
    for j in range(len(arr)-2):
        print(arr[j+2]*num,end="")
    print()