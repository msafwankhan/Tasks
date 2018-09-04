prime = [x for x in range(3,101) for y in range(3, x//2) if x % y!=0]

print(prime)