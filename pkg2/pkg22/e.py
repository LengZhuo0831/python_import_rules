import os, sys
print(os.path.abspath('.'))
print(sys.path)

import pkg2, main



from ..pkg11 import c1

print(c1.name)

print('eeeeee')