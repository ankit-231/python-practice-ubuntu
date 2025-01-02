height = 5
  
# Number of character width in each line 
  
width = (2 * height) - 1
  
# Function to find the absolute value 
# of a number D 
  
def abs(d): 
    if d < 0: 
        return -1*d 
    else: 
        return d 

# Function to print the pattern of 'O' 
def printO() : 
    space = height // 3
    width = height // 2 + height // 5 + space + space 
    for i in range(0,height) : 
        for j in range(0,width + 1) : 
            if ( j == width - abs(space) or j == abs(space)): 
                print("*",end="") 
            elif( (i == 0 or i == height - 1) and j > abs(space) and j < width - abs(space) ) : 
                print("*",end="") 
            else : 
                print(end=" ") 
  
        if( space != 0 and i < height // 2) : 
            space = space -1
        elif ( i >= (height // 2 + height // 5) ) : 
            space = space -1
        print() 
        

def printA(): 
  
    n = width // 2
    for i in range(0, height): 
        for j in range(0, width+1): 
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))): 
                print("*", end="") 
            else: 
                print(end=" ") 
        print() 
        n = n-1

def printW() : 
    counter = height // 2
    for i in range(0,height) : 
        print("*",end="") 
        for j in range(0,height+1) : 
            if ( j == height ): 
                print("*",end="") 
            elif ( (i >= height // 2) and (j == counter or j == height - counter - 1) ) : 
                print("*",end="") 
            else : 
                print(end=" ") 
        if( i >= height // 2) : 
            counter = counter + 1
        print() 
  

# printA()
# printO()
printW()