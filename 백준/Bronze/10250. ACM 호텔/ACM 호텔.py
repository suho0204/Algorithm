t = int(input())
for i in range(t):
    h, w, n = map(int,input().split())
    a = n % h
    b = int(n/h)
    if a == 0:
        a = h
    else:
        b = b + 1
    if b < 10:
        arr = (str(a)+'0'+str(b))
        arr2 = int(arr)
        print(arr2)
    else:
        arr = str(a)+str(b)
        arr1 = int(arr)
        print(arr1)