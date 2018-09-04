numbers_list = [x for x in range(101)]
even = [x for x in range(0,101) if x %2 ==0]
odd = [x for x in range(1,101) if x%2 != 0]


def is_prime(number):
    if number>1:
        if number == 2:
            return True
        if number %2 == 0:
            return False
        for i in range(3,number//2, 2):
            if number % i == 0:
                return False
        return True
    return False





print('Even ->',even)
print('Odd ->',odd)
print('Prime ->',[a for a in numbers_list if is_prime(a)])