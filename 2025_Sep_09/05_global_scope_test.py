a = [10, 20, 30]

def testfn():
    print("In testfn: a =", a)
    #a = [1000, 20, 30]
    a[0] = 1000
    a.append(40)
    print("In testfn after modification: a =", a)

testfn()
print("In global scope: a =", a)