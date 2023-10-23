def add(*args):
    amount = 0
    for n in args:
        amount += n
    return amount

print(add(3, 5, 7, 8, 1 , 3, 5, 6))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items()
    #       print(key)
    #       print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(2, add=3, multiply=5)



# Using it in a class

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan")
print(my_car.seats)