a = int(input('numerator '))
b = int(input('denominator '))
try:
    c = a/b
    print('division yield = ', c)
except Exception as e:
    print('Error occourde -> ', e)
    print('Exceptio Type', type(e).__name__)