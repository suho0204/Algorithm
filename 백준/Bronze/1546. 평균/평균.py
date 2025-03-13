n = int(input())
score = list(map(int,input().split()))

m = max(score)
sum = 0
for i in range(len(score)):
    score[i] = score[i]/m*100

for j in range(len(score)):
    sum += score[j]

print(sum/len(score))