array = [4,8,2,2,2,6,9]
non_duplicate = []
duplicate = []
for a in array:
    if a not in non_duplicate:
        non_duplicate.append(a)
    else:
        duplicate.append(a)

print("Array without duplicates is -> ",non_duplicate)
print("The duplicates in the array were ->", duplicate)