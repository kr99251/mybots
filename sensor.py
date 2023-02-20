import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName) -> None:
        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if x == 999:
            print(self.values)

    def Save_Values(self):
        numpy.save("data/" + self.linkName + ".npy", self.values)