import argparse

parser = argparse.ArgumentParser()

parser.add_argument('n1 ', type=int, help='the first number')
parser.add_argument('n2 ', type=int, help='the second number')
parser.add_argument('ops ', type=str, help='the ops')

args = parser.parse_args()
#print(args.__dict__['n1'])

for k in args.__dict__:
    print(k)
    print(args.__dict__[k])

