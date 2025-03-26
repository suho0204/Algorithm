import sys
n = int(sys.stdin.readline())
num = 0
mo = 666
while True:
    if '666' in str(mo):
        num += 1
    if num == n:
        break
    mo += 1

print(mo)                
