x = int(input())
score = 0
num = 0
for i in range(x):
    arr = input()
    for j in range(len(arr)):
        if arr[j] == 'O':
            num = num + 1
        else:
            num = 0
        score = score + num
    print(score)
    score = 0
    num = 0