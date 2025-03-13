n, k = map(int,input().split())
a = 1
if k == 0:
    a = 1
else:
    for i in range(k):
        a = a*(n-i)
    for j in range(k):
        a = a/(k-j)

print(int(a))