sar = float(input("Enter the side length of the square which will also act as the radius of the circle: "))
area_of_square = sar ** 2
area_of_cirlce = (22/7)*(sar ** 2)

if area_of_cirlce > area_of_square:
    print("Circle has a greater area")

else:
    print("Square has a greater area.")

print("Area of circle= %f squts\nArea of square= %f squts" % (area_of_cirlce,area_of_square))