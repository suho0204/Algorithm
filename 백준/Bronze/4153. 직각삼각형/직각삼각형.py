while True:
    a, b, c = map(int,input().split())
    if a==0 & b==0 &c==0:
        break
    elif ((a*a)+(b*b)==(c*c)) | ((c*c)+(b*b)==(a*a)) | ((a*a)+(c*c)==(b*b)):
        print("right")
    else:
        print("wrong")