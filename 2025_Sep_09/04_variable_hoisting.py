
def testfn():
    global a
    a = 200   # This variable is hoisted to global scope. AVOID THIS IN PYTHON!!!
    print("In testfn after modification: a =", a)

testfn()
print("In global scope: a =", a)