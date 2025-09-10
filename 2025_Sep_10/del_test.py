class User:
    def __new__(cls):
        obj = super().__new__(cls)
        print("__new__ invoked: obj =", obj)
        return obj
    
    def __init__(self):
        print("__init__ invoked: self=", self)
        
    def __del__(self):
        print("__del__ method invoked on", self)
    
u = User()
u1 = u
u2 = u1
del u
print("u deleted")
u1 = 100
print("u1 changed to", u1)
u2 = "Hello world"
print("u2 changed to", u2)