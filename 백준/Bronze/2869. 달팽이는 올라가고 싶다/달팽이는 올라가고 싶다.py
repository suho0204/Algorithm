a, b, v = map(int,input().split())
days = 0
if (v-a) % (a-b) ==0:
    days = (v-a)//(a-b)+1
else:
    days = (v-a)//(a-b)+2
print(days)
