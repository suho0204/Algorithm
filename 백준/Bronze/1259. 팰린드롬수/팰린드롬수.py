while True:
    arr = input()
    if arr == '0':
        break
    for i in range (len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            print("no")
            break
    else:
        print("yes")