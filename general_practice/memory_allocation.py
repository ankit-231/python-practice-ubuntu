# import sys
# x = 12312312332
# print(sys.getsizeof(x))

a = ["a", "aa"]
b = [a, 1]
a.append(b)

print(a, "a")
print(b, "b")

import gc

ncycles = gc.collect()  # Forces garbage collection
print("Collected", ncycles, "cycles")
