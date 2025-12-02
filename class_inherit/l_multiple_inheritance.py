class Father:
    def skills(self):
        print('I can earn')

class Mother:
    def skills(self):
        print('I can cook')

class Child(Father, Mother):
    def skills(self):
        print('I can entertain')
        Father.skills(self)


if __name__ == '__main__':
    abc = Child()
    abc.skills()
    Mother.skills(abc)