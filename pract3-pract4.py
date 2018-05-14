"""
my_foods = ['pizza', 'falafel', 'carrot cake', 'grilled cheese']
friends_foods = my_foods[:]


my_foods.append('cannoli')
friends_foods.append('ice cream')


print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friends_foods)



print("The first three items in my list are: ")
print(my_foods[:3])

print("Three items from the middle of my list are: ")
print(my_foods[int(len(my_foods) / 2 - 1) : int(len(my_foods) / 2 + 2) ])


print("Three items from the end of my list are: ")
print(my_foods[len(my_foods) - 3:])



pizza = ['cheese', '3-cheese', '4-cheese', 'veggie supreme', 'mushrooms']

friend_pizza = pizza[:]

pizza.append('pepper pizza')

friend_pizza.append('super-mushroom')

print("My favorite pizzas are: ")
for zas in pizza:
    print(zas, end = "" + ", ")

print("\nMy friends favorite pizzas are: ")
for zas in friend_pizza:
    print(zas, end = "" + ", ")

"""


food_tuple = ('mac and cheese', 'eggs', 'fruit', 'coffee', 'waffles')

for food in food_tuple:
    print(food)

# food_tuple[0] = 'bananas' - tuple object does not support item assignment

food_tuple = ('bread', 'watermelon')

print('-----------')

for food in food_tuple:
    print(food)




