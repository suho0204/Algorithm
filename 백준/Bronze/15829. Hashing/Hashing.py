n = int(input())
arr = input()
num = []
for i in range(len(arr)):
    num.append(ord(arr[i])-96)
sum = 0
for j in range(len(num)):
    sum += num[j]*(pow(31, j))
print(sum)