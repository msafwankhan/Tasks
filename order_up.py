a= input("Enter a number: ")
b= input("Enter a number: ")
c= input("Enter a number: ")

if a>b and a>c:
    if b>c:print("Order is:",a,b,c)
    elif c>b:print("Order is:",a,c,b)

elif b>a and b>c:
    if a>c:print("Order is:",b,a,c)
    elif c>a:print("Order is:",b,c,a)

elif c>a and c>b:
    if b>a:print("Order is:",c,b,a)
    elif a>b:print("Order is:",c,a,b)





