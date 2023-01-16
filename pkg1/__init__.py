# import sys
# import os
# # print(os.path.abspath(__package__))
# sys.path.append(os.path.abspath(__package__))
# import c1

pkg1_name = "My name is pkg1"
from .c1 import name as c1_name

