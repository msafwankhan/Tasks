number = int(input("Enter a two digit number: "))

if number>=10:
    print("The sum of the digits %d and %d is %d"%(number // 10,number % 10,((number % 10)+number // 10)))


else:
    print("Please enter a two digit number")