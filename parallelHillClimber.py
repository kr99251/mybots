from solution import SOLUTION
import constants
import copy
import os
import numpy

class PARALLEL_HILL_CLIMBER:
    def __init__(self) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(constants.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.fitness = numpy.zeros((constants.populationSize, constants.numberOfGenerations))
        self.generation = 0

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
        print(self.fitness)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.generation += 1
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if (self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]

    def Print(self):
        print()
        for key in self.parents:
            print(self.parents[key].fitness, self.children[key].fitness)
        print()

    def Show_Best(self):
        lowest = 50
        for key in self.parents:
            if self.parents[key].fitness < lowest:
                lowest = self.parents[key].fitness
        self.parents[key].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            self.fitness[key][self.generation] = solutions[key].fitness