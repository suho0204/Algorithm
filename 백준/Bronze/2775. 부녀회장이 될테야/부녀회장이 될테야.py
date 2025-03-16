t = int(input())

arr =[]
arr1 =[]
for _ in range(t):
    sum = 0
    num = 0
    k=int(input())
    n=int(input())
    for a in range(1,k+1):
        for b in range(1,n+1):
            if a == 1:
                sum += b
                arr.append(sum)
            else:
                sum += arr1[b-1]
                arr.append(sum)
        arr1 = arr[:]
        sum = 0
        arr = []
    print(arr1[n-1])