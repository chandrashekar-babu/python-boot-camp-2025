
data = []

while True:
    v = input("Enter a value: ")
    if not v: break
    data.append(v)


done = True
while data:
    v = data.pop()
    if v < 0:
        done = False
        break
    print "Value =", v


if not done:
    print "Did not remove all elements..."

