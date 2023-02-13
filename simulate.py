from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()

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





# numpy.save("data/backLegSensorVals.npy", c.backLegSensorValues)
# numpy.save("data/frontLegSensorVals.npy", c.frontLegSensorValues)
# p.disconnect()