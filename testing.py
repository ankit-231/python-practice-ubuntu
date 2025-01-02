def a(*args, **kwargs):
    print(args)
    print(kwargs)


c = 1 & 2 | 3

d = (4, 5, 6)

a(1, 2, 3, c, *d, a=1, b=2, c=3)
