arr = []
for i in range(9):
    arr.append(int(input()))
big = arr[0]
for i in range(8):
    if big < arr[i+1]:
        big = arr[i+1]

print(big)

for i in range(9):
    if arr[i] == big:
        print(i+1)