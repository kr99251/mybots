import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

amplitude = numpy.pi/4
frequency = 10
phaseOffset = 0

amplitude2 = numpy.pi/4
frequency2 = 10
phaseOffset2 = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
targetAngles = amplitude * numpy.sin(frequency * targetAngles + phaseOffset)

targetAngles2 = numpy.linspace(0, 2*numpy.pi, 1000)
targetAngles2 = amplitude2 * numpy.sin(frequency2 * targetAngles2 + phaseOffset2)

# numpy.save("data/targetAngles.npy", targetAngles)
# numpy.save("data/targetAngles2.npy", targetAngles2)


for x in range(1000):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[x],
        maxForce = 100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles2[x],
        maxForce = 100)
    time.sleep(1/240)

numpy.save("data/backLegSensorVals.npy", backLegSensorValues)
numpy.save("data/frontLegSensorVals.npy", frontLegSensorValues)
p.disconnect()
