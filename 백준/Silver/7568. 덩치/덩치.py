n = int(input())
w = []
h = []
for i in range(n):
    x, y = map(int,input().split())
    w.append(x)
    h.append(y)
rate = []
for i in range(n):
    num = 0
    for j in range(n):
        if (w[i] < w[j]) & (h[i] < h[j]):
            num += 1
    rate.append(num+1)
print(*rate)