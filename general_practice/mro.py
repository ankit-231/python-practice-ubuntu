# Method Resolution Order in Python


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# print(D.__mro__)
print(D.mro())
