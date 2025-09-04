#!/usr/bin/env python

print(__name__) # `__name__` is a special variable that 
                # represents the name of the module running
                # this program

num = int(input("Enter a number: ")) 
for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    print(num, "x", i, "=", num*i)
