stack = [22, 10, 33, 10, 55, 66, 77]

# Pop each value off the stack and process them.
# Abort if empty value is found.

while stack:
    value = stack.pop()
    if not value:
        print("Found an empty value, breaking out abruptly!")
        break
    # process_something(value)
else:
    print("Processed all elements")


print("End of program")

