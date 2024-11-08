class Car:
    amount_car = 0
    def __init__(self, manufacture, model, hp):
        self.manufacture = manufacture
        self.model = model
        self.hp = hp
        Car.amount_car += 1
    def print_in4(self) :
        print("Manufacture: {}, Model: {}, HP: {}\n".format(self.manufacture, self.model, self.hp))
    def print_car_amount(self):
        print("Có : %d chiếc xe" %Car.amount_car)
    def __del__ (self) :
        print("Object gets deleted")
        Car.amount_car -= 1
mycar1 = Car("Tesla", "Model X", 600)
myCar2 = Car("BMW", "X3", 200)
myCar3 = Car("VW", "Golf", 100)
myCar4 = Car("Porsche", "911", 520)
del myCar3
mycar1.print_car_amount(), myCar2.print_in4()