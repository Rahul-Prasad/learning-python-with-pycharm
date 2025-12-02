class Human:
    def __init__(self, name, occupation):
            self.name = name
            self.occupation = occupation

    def print_profession(self):
        if (self.occupation == 'tennis player'):
            print('I play a sport')
        if (self.occupation == 'actor'):
            print('I act')

    def say_hello(self):
        print('Hello, my name is ' + self.name)

if __name__ == '__main__':
    tom = Human('Tom', 'actor')
    maria = Human('Maria', 'tennis player')

    tom.say_hello()
    tom.print_profession()

    maria.say_hello()
    maria.print_profession()