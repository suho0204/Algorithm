n = int(input())
i = 1
x = 1
while True:
    if n <= x:
        break
    else:
        x = x + 6*i
        i += 1
print(i)         

