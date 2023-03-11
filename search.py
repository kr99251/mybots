import os
from hillclimber import HILL_CLIMBER

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")

h = HILL_CLIMBER()
h.Evolve()
h.Show_Best()

# os.system("python simulate.py GUI")