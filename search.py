import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
numpy.save('fitness_matrix.npy', phc.fitness)
# phc.Show_Best()
