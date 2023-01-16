from a import a, A, AA, a_function
# print(a)
# print(A)
# aa = AA()
# print(aa)
# a_function()

# import b
# print(b.name)

# import pkg1.c1 as c1
# print(c1.name)

import pkg1
print(pkg1.pkg1_name)
print(pkg1.c1.name)

import pkg1.util.util1 as util1
print(util1.uname)

import os, sys
print(os.path.abspath('.'))
print(sys.path)

import pkg2.d

# import pkg2.pkg22.e
import pkg2.pkg23.f
