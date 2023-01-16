
# import sys
# import os
# print(os.path.abspath('.'))
# sys.path.append(os.path.abspath('.'))

from pkg1 import c1
print(c1.name)


from a import a, A, AA, a_function

print(a)
print(A)
aa = AA()
print(aa)
a_function()

from .pkg11 import c1
print(c1.name)