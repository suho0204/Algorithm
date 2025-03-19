import sys
def roundup(number):
    if(number - int(number)) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

n = int(input())

if n == 0:
    print(0)
else:
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))
    arr.sort()
    num = roundup(n*0.15)
    
    print(roundup(sum(arr[num:n-num])/len(arr[num:n-num])))