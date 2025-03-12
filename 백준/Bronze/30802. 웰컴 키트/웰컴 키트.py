N = int(input())
list = list(map(int,input().split()))
T, P = map(int,input().split())
T1 = 0

for  i in list:
    if i == 0:
        continue
    elif i%T==0:
        T1+= i//T
    else:
        T1+=i//T+1

print(T1)
P1 = int(N/P)
P2 = N%P
print(P1,P2)