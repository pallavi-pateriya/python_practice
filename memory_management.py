import sys
import gc

"""Reference counting """
a = [1, 2, 3]
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
del a
del b


"""using garbage collector to clean up circular references"""
a = [1,2,3]
b = [4,5,6]
a.append(b)
b.append(a)  # circular reference

del a
del b
gc.collect()  # Garbage collector cleans up the cycle
