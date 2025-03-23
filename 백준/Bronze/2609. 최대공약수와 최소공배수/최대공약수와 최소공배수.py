a, b = map(int,input().split())
if a > b:
    for i in range(b):
        num = b-i
        if ((a % num) == 0)&((b % num)==0):
            print(num)
            print((a//num)*(b//num)*num)
            break
elif a < b:
    for i in range(a):
        num = a-i
        if ((a % num) == 0)&((b % num)==0):
            print(num)
            print((a//num)*(b//num)*num)
            break
else:
    print(a)
    print(b)