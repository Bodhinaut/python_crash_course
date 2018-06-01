# 8 - 15 && 8 - 16 && 8- 17
from  print_models import print_models as pm
from show_models import show_completed_models as sm

unprinted_designs = ['iphone case', 'robo pendant', 'octothorpe']
completed_models = []

pm(unprinted_designs, completed_models)
sm(completed_models)