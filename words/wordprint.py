# Number of lines for the alphabet's pattern

height = 5

# Number of character width in each line

width = (2 * height) - 1

# Function to find the absolute value
# of a number D


def abs(d):
    if d < 0:
        return -1 * d
    else:
        return d


# Function to print the pattern of 'E'
def printE():

    for i in range(0, 5):
        print("*", end="")
        for j in range(0, 5):
            if (i == 0 or i == 4) or (i == 2 and j <= 2):
                print("*", end="")
            else:
                continue
        print()


# printE()

def temp():
    for i in range(0, 5):
        print("a", end="")
        
    print()
# temp()
printE()
