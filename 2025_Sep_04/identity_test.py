a = 300000000
b = 300000000
print(a is b)  # False, because 300 is outside the small integer cache range
print(a == b)  # True, because values are equal
# Identity equality vs Value equality
# 'is' operator checks if both variables point to the same object in memory
# '==' operator checks if the values of the variables are equal