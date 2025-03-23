arr1 = input()
arr2 = input()
arr3 = input()

if arr1.isdigit():
    a = int(arr1)
    b = a+1
    c = a+2
if arr2.isdigit():
    b = int(arr2)
    a = b-1
    c = b+1
if arr3.isdigit():
    c = int(arr3)
    a = c-2
    b = c-1
num = c+1
if ((num%3)==0)&((num%5)!=0):
    print("Fizz")
elif ((num%3)!=0)&((num%5)==0):
    print("Buzz")
elif ((num%3)==0)&((num%5)==0):
    print("FizzBuzz")
else:
    print(num)