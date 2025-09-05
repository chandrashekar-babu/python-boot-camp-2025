a = 0
limit = 5
max_value = int(input("Enter maximum value: "))

while a < limit:
    print("Counting", a)
    a += 1
    if a >= max_value:
        break
else:
    print("Max limit reached")

print("End of program")
