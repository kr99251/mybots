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
        targetAngles = c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * c.targetAngles + c.phaseOffsetBackLeg)
        targetAngles2 = c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * c.targetAngles + c.phaseOffsetFrontLeg)
        for x in range(1000):
            p.stepSimulation()
            self.robot.Sense(x)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robotId,
                jointName = "Torso_BackLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = targetAngles[x],
                maxForce = 100)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robotId,
                jointName = "Torso_FrontLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = targetAngles2[x],
                maxForce = 100)
            time.sleep(1/240)
            
    def __del__(self):
        p.disconnect()

