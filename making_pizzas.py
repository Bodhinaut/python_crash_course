# import all funcitons in module
from pizza import *

import pizza
# below is example on how to import specific function
from pizza import make_pizza
# With this syntax, you don’t need to use the dot notation when you call a
# function. Because we’ve explicitly imported the function make_pizza() in the
# import statement, we can call it by name when we use the function.
from pizza import make_pizza as mp
# Here we give the function make_pizza() an alias, mp(), by importing
# make_pizza as mp. The as keyword renames a function using the alias you
# provide:

import pizza as p
# You can also provide an alias for a module name. Giving a module a short
# alias, like p for pizza, allows you to call the module’s functions more quickly.
# Calling p.make_pizza() is more concise than calling pizza.make_pizza():


p.make_pizza(10, 'swiss')
pizza.make_pizza(16, 'veggie lovers')
# imported specific function example..
make_pizza(24, 'extra cheese', 'green peppers', 'onions')
mp(12, 'banana peppers')