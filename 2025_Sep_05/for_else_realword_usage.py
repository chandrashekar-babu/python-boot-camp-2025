data = 44, 26, 48, 32, 13, 18, 2, 38

# Search for an odd number in a collection
for value in data:
    if value & 1:
        print "Odd number found:", value
        break
else:
    print "The collection has no odd numbers"

print "End of program"

