class Accidents(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_msg(self):
        print('Accident occured ', self.msg)


a = input('enter a number ')
try :
    if int(a) < 0 :
        raise Accidents("negative number")
except Accidents as e:
    e.print_msg()

