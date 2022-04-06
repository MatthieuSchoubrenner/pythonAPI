class Car:
    counter = 0
    def __init__(self, name, model, max_speed, kms, color):
        self.name = name
        self.model = model
        self.max_speed = max_speed
        self.kms = kms
        self.color = color

        Car.counter += 1

c = Car ('Renault Clio', 'Clio', 170, 25000, 'bleu')
c1 = Car ('Renault Clio', 'Clio', 170, 25000, 'bleu')
c2 = Car ('Renault Clio', 'Clio', 170, 25000, 'bleu')


class Boat:
    counter = 0
    def __init__(self, name, model, max_speed, kms, color):
        self.name = name
        self.model = model
        self.max_speed = max_speed
        self.kms = kms
        self.color = color

        Boat.counter += 1

b = Boat ('Titanic', 'Titanic', 500, 25000, 'noir')
b1 = Boat ('Titanic', 'Titanic', 500, 25000, 'noir')


class Motorbike:
    counter = 0
    def __init__(self, name, model, max_speed, kms, color):
        self.name = name
        self.model = model
        self.max_speed = max_speed
        self.kms = kms
        self.color = color

        Motorbike.counter += 1

m = Motorbike ('Yamaha', 'viper', 400, 700, 'red')
m1 = Motorbike ('Yamaha', 'viper', 400, 700, 'red')
m2 = Motorbike ('Yamaha', 'viper', 400, 700, 'red')
m3 = Motorbike ('Yamaha', 'viper', 400, 700, 'red')
m4 = Motorbike ('Yamaha', 'viper', 400, 700, 'red')
m5 = Motorbike ('Yamaha', 'viper', 400, 700, 'red')


class Plane:
    counter = 0
    def __init__(self, name, model, max_speed, kms, color):
        self.name = name
        self.model = model
        self.max_speed = max_speed
        self.kms = kms
        self.color = color

        Plane.counter += 1

p = Plane ('Airbus A380', 'A380', 900, 700000, 'white')
p1 = Plane ('Airbus A380', 'A380', 900, 700000, 'white')
p2 = Plane ('Airbus A380', 'A380', 900, 700000, 'white')

