color = "Red"

def start():
    print("Start of the program")

class Car:
    color = "White" # Class attribute do not participate in scope resolution for instance methods

    def __init__(self):
        color = "Green" # A Local variable in __init__ method
        print("Inside __init__:", color)
        self.color = "Black" # Instance attribute

    def start(self):
        print("Started the car")

    def drive(this):
        start()
        this.start()
        print("Driving a", color, "car")
        print(f"{this.color=}")
        print(f"{Car.color=}")


c1 = Car()
c1.drive()
