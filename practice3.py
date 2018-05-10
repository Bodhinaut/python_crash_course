"""

magic = ['fire','water','earth','wind']


for spells in magic:
    print (spells)

for spells in magic:
    print(spells)

for spells in magic:
    print(spells)

for x in magic:
    print(x)

for y in magic:
    print(y)


print('----------------------------------------------------')


for spells in magic:
    print(spells.upper() + ", is a usable spell!")
    print("Wizard, please cast " + spells.title() + "!\n")

print("The spells were cast successfully!")



pizza = ['cheese','extra cheese','veggie\'za']

for pizzas in pizza:
    print(pizzas.title() + " pizza is one of my favorite things to eat!")
print("My wife and I, are in LOVE with pizza!")

print('---------------------------------------------------------------')

animals = ['dogs','cats','chinchillas']

for pets in animals:
    print(pets.title() + " would make a great pet!")
print("These animals are all well domesticated!")

print('---------------------------------------------------------------')


numbers = list(range(1,6) )

print(numbers)


numbers_even = list(range(2, 20, 2) )
print(numbers_even)


squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)


print(min(numbers) )
print(max(numbers) )
print(sum(numbers) )


sqs = [value ** 2 for value in range(1,11) ]
print (sqs)

squares = [number ** 2 for number in range(1,100)]
print (squares)

squares = [value ** 2 for value in range(1,11)]
print (squares)




range1_20 = [print(values) for values in range(1,21)]

for value in range(1,21):
    print (value)


one_mil = list(range(1, 1000001) )


# for values in one_mil:
#    print (values)



print(sum(one_mil) )
print(min(one_mil) )
print(max(one_mil) )





odd_num = list(range(1,20,2) )
print (odd_num)
for values in odd_num:
    print(values)




# threes = [print(values * 3) for values in range(3, 30)]

#for values in range(3,30):
#    print(values * 3)


cubes_1_10 = [print(values ** 3) for values in range(1,10) ]



for values in range(1,11):
    print (values ** 3)

"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[3:] )
















