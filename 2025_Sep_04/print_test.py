#!/usr/bin/env python

from sys import stderr

print("Hello world")

print("This is a test string", file=stderr)

#with open("output.txt", "w") as outfile:
#    print("this is a new string", file=outfile)

outfile = open("output.txt", "a")
print("this is a new string", file=outfile)
outfile.close()




