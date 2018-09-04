a= input("Enter a number: ")
b= input("Enter a number: ")
c= input("Enter a number: ")

if a>b and a>c:
    print("Max is",a)
    if b>c:print("Min is:",c)
    elif c>b:print("Min is:",b)

elif b>a and b>c:
    print("Max is:",b)
    if a>c:print("Min is:",c)
    elif c>a:print("Min is:",a)

elif c>a and c>b:
    print("Max is:",c)
    if b>a:print("Min is:",a)
    elif a>b:print("Min is:",b)

