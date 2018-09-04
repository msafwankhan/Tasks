for row in range(0, 3):
    for space in range(1, 2 - row + 1):
        print(" ", end='')
    for number in range(1, 2 * (row + 1)):
        print("*", end="")
    print()

print("-"*5 + "Another Method" + "-"*5)

name = ["*"*(x+1) for x in range(4,-1,-1) if (x+1)%2!=0]
for i in range(2,-1,-1):
	    print(" "*i+name[i])