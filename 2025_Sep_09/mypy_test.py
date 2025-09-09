

#def square(x: Union[int, float, complex]) -> Union[int, float, complex]:
#    return x * x

def square(x: int | float | complex) -> int | float | complex:
    return x * x

message: str = "Hello, World!"

print(message)

print(square(2))
print(square(3.2))
print(square(4+5j))
print(square("Hello"))

message = 100
print(message)
