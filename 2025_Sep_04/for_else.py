nums = 44, 55, 66, 77, 33, 22, 56, 78, 76, 55

search = int(raw_input("Enter number to search: "))

#for n in nums:
#    if n == search:
#       print search, "found"
#       break
#else:
#    print search, "not found"

#if search in nums:
#   print search, "found"
#else:
#  print search, "not found"

print search, "found" if search in nums else "not found"
