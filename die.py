"""Die class that implemnets roling a die"""
from random import randint
# 9 - 13 
class Die():
	"""Default ctr"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print("A roll of the die... you get: " + str(randint(1, self.sides) ) )
		

die = Die()
die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.roll_die()