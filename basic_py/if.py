num_s = input("Enter a number: ")
num = int(num_s)
if (num%2 == 0):
    print(num, "is even")
else:
    print(num, "is odd")



Indian_dishes = ['pulao', 'dal', 'curry', 'bhatura']
Chinese_dishes = ['manchurian', 'veg_chilly', 'noodles']
Italian_dishes = ['pizza', 'pasta', 'rizotto']

Dish = input("Enter a dish: ")
if (Dish in Indian_dishes): print(Dish, "is an Indian dish")
elif (Dish in Chinese_dishes): print(Dish, "is a Chinese dish")
elif (Dish in Italian_dishes): print(Dish, "is a Italian dish")
else : print(Dish, "is not an menu")
