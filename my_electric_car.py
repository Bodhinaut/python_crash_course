from car import Car, ElectricCar

my_beetle = Car('volkswagen','beetle', 2016)

my_tesla = ElectricCar('tesla', 'model s', 2017)

print(my_tesla.get_descriptive_name() )
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print(my_beetle.get_descriptive_name() )

# or you can import the entire module and access the classses you need using dot notaion

"""
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name() )

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name() )
"""