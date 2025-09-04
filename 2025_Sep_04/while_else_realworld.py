
data = []

while True:
    v = input("Enter a value: ")
    if not v: break
    data.append(v)


while data:
    v = data.pop()
    print "Value =", v
    if v < 0:
        print "could not remove all elements"
        break
else:
    print "removed all elements..."

print "Data =", data

