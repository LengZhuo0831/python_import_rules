a = "I'm a"
A = "I'm A"

class AA:
    def __init__(self):
        self.aa = "I'm class AA"
    
    def __str__(self):
        return self.aa

def a_function():
    print("this is a function in a.py")

print("this is file a.py, and a:",a)
if __name__=='__main__':
    print(print("this is file a.py, and A:",A))

