from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy

class SIMULATION:
    def __init__(self) -> None:
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run():
        # targetAngles = c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * c.targetAngles + c.phaseOffsetBackLeg)
        # targetAngles2 = c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * c.targetAngles + c.phaseOffsetFrontLeg)
        for x in range(1000):
            # p.stepSimulation()
            # c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = "Torso_BackLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAngles[x],
            #     maxForce = 100)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = "Torso_FrontLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAngles2[x],
            #     maxForce = 100)
            # time.sleep(1/240)
            print(x)