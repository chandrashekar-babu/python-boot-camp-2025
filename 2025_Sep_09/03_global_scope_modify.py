a = 100

def testfn():
    global a
    print("In testfn: a =", a) # 'a' was now determined to be a global variable 
                               # during compile-time because of the 'global' statement
    a = 200
    print("In testfn after modification: a =", a)

testfn()
print("In global scope: a =", a)