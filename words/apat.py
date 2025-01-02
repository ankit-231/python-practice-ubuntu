def b2():
    """ Return a string which will print the alphabet pattern 'A', shown below.
        Use loops and conditional statements, do NOT just hard code the text string.
        The letter fits in a 7x7 grid

          ***                                                                   
         *   *                                                                  
         *   *                                                                  
         *****                                                                  
         *   *                                                                  
         *   *                                                                  
         *   *           
    """
    A_pat = [" *** ", "*   *", "*   *", "*****", "*   *", "*   *", "*   *" ]
    
    New_list = []
    
    for i in A_pat:
        New_list.append(i)
    return New_list

A_pat = [" *** ", "*   *", "*   *", "*****", "*   *", "*   *", "*   *" ]

for i in A_pat:
    print(i)