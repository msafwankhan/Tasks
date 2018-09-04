for i in range(4):
    if i%2==0:
        for j in range(7):
            print("+",end="")
        print()
    else:
        for j in range(7):
            print("*",end="")
        print()

print("\nNew Line\n")
for i in range(2):
    for j in range(7):
        print("+", end="")
    print()
    for k in range(7):
        print("*", end="")
    print()
