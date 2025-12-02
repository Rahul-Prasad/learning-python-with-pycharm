class Vehical:
    def general_usage(self):
        print('General usage is transport')

class Car(Vehical):
    def __init__(self, name):
        self.name = name

    def printusage(self):
        print('Hi I am a Car of type', self.name)
        self.general_usage()
        print('good for family')

class Bike(Vehical):
    def __init__(self, name):
        self.name = name

    def printusage(self):
        print('Hi I am a bike of type', self.name)
        self.general_usage()
        print('faster for singles or 2 people')

if __name__ == '__main__':
    p = Bike('pulsar')
    p.printusage()