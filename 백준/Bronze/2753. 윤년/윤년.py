x = int(input())
i = x % 4

if i != 0 :
    print(0)
elif (x % 100) == 0:
    if (x % 400) == 0:
        print(1)
    else :
        print(0)
else :
    print(1)