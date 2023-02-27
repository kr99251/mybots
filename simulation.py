from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self) -> None:
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for x in range(1000):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)
            time.sleep(1/240)
            
    def __del__(self):
        p.disconnect()

