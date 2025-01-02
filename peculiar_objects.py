class ParentA:

    simple_list = []

    def __init__(self):
        pass


aA = ParentA()
aA.simple_list.append("aA content")

bA = ParentA()
bA.simple_list.append("bA content")

# simple_list will be shared across all instances
print(aA.simple_list)
print(bA.simple_list)


class ParentB:

    def __init__(self, simple_list=[]):
        self.simple_list = simple_list


aB = ParentB()
aB.simple_list.append("aB content")

bB = ParentB()
bB.simple_list.append("bB content")

# simple_list will still be shared across each instance
print(aB.simple_list)
print(bB.simple_list)


class ParentC:

    def __init__(self):
        self.simple_list = []


aC = ParentC()
aC.simple_list.append("aC content")

bC = ParentC()
bC.simple_list.append("bC content")

# simple_list will will be unique across each instance
print(aC.simple_list)
print(bC.simple_list)
