from simulation import SIMULATION
simulation = SIMULATION()

# import pybullet as p
# import pybullet_data
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy
# import constants as c

# p.setGravity(0,0,-9.8)
# p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# targetAngles = c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * c.targetAngles + c.phaseOffsetBackLeg)
# targetAngles2 = c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * c.targetAngles + c.phaseOffsetFrontLeg)


# for x in range(1000):
#     p.stepSimulation()
#     c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = "Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles[x],
#         maxForce = 100)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = "Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles2[x],
#         maxForce = 100)
#     time.sleep(1/240)

# numpy.save("data/backLegSensorVals.npy", c.backLegSensorValues)
# numpy.save("data/frontLegSensorVals.npy", c.frontLegSensorValues)
# p.disconnect()