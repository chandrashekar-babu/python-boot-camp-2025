print("Hello world")

with open("out.txt", "w") as out:
    print("This is line 1", file=out)
    print("This is line 2", file=out)

