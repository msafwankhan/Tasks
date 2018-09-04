
def tree_printer(repeat):

    while repeat>0:

        for row in range(0,5):
            if row % 2 == 0 :
                ch = "*"
            else: ch = "^"

            for space in range(1, 4 - row + 1):
                print(" ", end='')
            for number in range(1, 2 * (row + 1)):
                print(ch, end="")
            print()
        for tr in range(3):
            for sp in range(3):
                print(" ",end="")
            for bark in range(3):
                print("|",end="")
            print()
        repeat -= 1


tree_printer(32)