arr = list(map(int,input().split()))
arr1 = [1,2,3,4,5,6,7,8]
arr2 = [8,7,6,5,4,3,2,1]
if arr == arr1:
    print("ascending")
elif arr == arr2:
    print("descending")
else:
    print("mixed")