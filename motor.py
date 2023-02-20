import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = numpy.linspace(0, 2*numpy.pi, 1000)
        self.amplitude = c.amplitude
        if self.jointName == 'Torso_BackLeg':
            self.frequency = c.frequency
        else:
            self.frequency = c.frequency/2
        self.offset = c.offset
        self.motorValues = self.amplitude * numpy.sin(self.frequency * self.motorValues + self.offset)

    def Set_Value(self, robot, x):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[x],
            maxForce = 100)

    def Save_Values(self):
        numpy.save("data/" + self.jointName + ".npy", self.motorValues)