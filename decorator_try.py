def outer(func):
    print("hehehe")

    # def wrapper(*args, **kwargs):
    #     return func

    return func


@outer
def inner(a, b):
    return a + b


# print(outer(inner(1, 2)))
print(inner(1, 2))


# def decorator(func):
#     def wrapper(*args):
#         # print("Logging the parameter of ", func, " is ", args)
#         return func(*args)

#     return wrapper


# @decorator
# def operation(x, y):
#     return x + y


# print(operation(5, 20))
