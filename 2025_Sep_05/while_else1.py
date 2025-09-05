nums = 33, 22, 44, 55, 66, 66, 77, 88, 11, 23, 32

v = int(raw_input("Enter a value to search: "))

#print "Value", "" if v in nums else "NOT", "found in collection"

if v in nums:
    print "Value found at", nums.index(v)
else:
    print "Value not found!"

print "Value", "found at " + str(nums.index(v)) if v in nums else "not found!"

print "End of program"


