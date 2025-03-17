n = int(input())
sum=1
count = 0
for i in range(n):
    sum= sum*(n-i)
arr = list(map(int,str(sum)))
for j in range(len(arr)):
    if arr[len(arr)-j-1] == 0:
        count += 1
    else:
        print(count)
        quit()
