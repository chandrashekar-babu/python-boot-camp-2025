a = 100

def testfn():
    print("In testfn: a =", a) # 'a' was determined to be a local variable 
                               # during compile-time because of the assignment below
    a = 200
    print("In testfn after modification: a =", a)

testfn()
print("In global scope: a =", a)