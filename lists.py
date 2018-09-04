L = [1, 1, 8, 3, 10, 6, 4, 2, 0, 8, 1, 6, 5, 8, 8, 0, 4, 6, 9, 6]

# First method
num = int(input("Enter a number to check: "))
count = 0

if num in L:
    print("Number is present")
    for x in range(len(L)):
        if L[x] == num:
            pos = x
            count += 1
    print("The number occurs {0} times. The last occurrence of '{1}' in the list is at index number {2}".format(
        str(count), str(num), str(pos)))


else:
    print("Number not present")

# Second method
flag = False
for a in range(len(L)):
    if int(L[a]) == num:
        flag = True
        break
print(flag)
# ----------------------------------------

# First method
print("\nLIST W/O DUPLICATES \n")
without_dupl = list(set(L))
print("The list without duplicate is:")
print(without_dupl)

# Second method
new_list = []
for i in L:
    if i not in new_list:
        new_list.append(i)
print(sorted(new_list))
# ----------------------------------------

print("\nFREQUENCY OF OCCURANCES\n")
my_dict = {}
for elem in L:
    if elem not in my_dict:
        my_dict[elem] = 1
    else:
        my_dict[elem] += 1
print(my_dict)
# ----------------------------------------

# First method
print("\nLIST ROTATION\n")
rotated_list = L.copy()
rotation = int(input("Enter the number of rotations: "))
for _ in range(rotation):
    buffer = rotated_list.pop(0)
    rotated_list.append(buffer)
print(rotated_list)

# Second method
new_L = L.copy()
for _ in range(rotation):
    for i in range(len(L) - 1):
        new_L[i], new_L[i + 1] = new_L[i + 1], new_L[i]
print(new_L)

# Third method
new_L2 = L.copy()
for _ in range(rotation):
    temp = new_L2[0]
    new_L2 = new_L2[1:]
    new_L2.append(temp)
print(new_L2)
