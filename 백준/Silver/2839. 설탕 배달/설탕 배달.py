n = int(input())
if n < 5:
    if n == 3:
        print(1)
    else:
        print(-1)
else:
    if n == 7:
        print(-1)
    elif (n % 5) == 3:
        print((n//5)+1)
    elif (n % 5) == 1:
        print((n//5)+1)
    elif (n % 5) == 4:
        print((n//5)+2)
    elif (n % 5) == 2:
        print((n//5)+2)
    elif (n % 5) == 0:
        print(n//5)
    else:
        print(-1)