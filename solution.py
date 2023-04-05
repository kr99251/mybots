import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, id) -> None:
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myId = id

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system('python simulate.py ' + directOrGUI + " " + str(self.myId) + " &")
        fitnessFileName = "fitness" + str(self.myId) + ".txt"
        f = open(fitnessFileName)
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        self.fitness = float(f.read())
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system('python simulate.py ' + directOrGUI + " " + str(self.myId) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myId) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        time.sleep(0.05)
        f = open(fitnessFileName)
        self.fitness = float(f.read())
        f.close()
        os.system("rm " + fitnessFileName)

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,5,0.5], size=[1,1,1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])
        pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0.25,-0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2", type="revolute", position=[0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[-0.25,-0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[0.25,0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="Torso", child="FrontLeg2", type="revolute", position=[0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[-0.25,0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg1", pos=[-0.5, 0.25, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-0.5, -0.25, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg1", pos=[0.5, 0.25, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0.5, -0.25, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute", position=[0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0.25,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute", position=[0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[-0.25,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute", position=[0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0.25,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute", position=[0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[-0.25,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="LeftLeg1_LeftLowerLeg1", parent="LeftLeg1", child="LeftLowerLeg1", type="revolute", position=[-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg1", pos=[0,0.25,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute", position=[-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0,-0.25,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="RightLeg1_RightLowerLeg1", parent="RightLeg1", child="RightLowerLeg1", type="revolute", position=[1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg1", pos=[0,0.25,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute", position=[1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0,-0.25,-0.5], size=[0.2,0.2,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "FrontLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "FrontLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "BackLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "BackLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "LeftLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "LeftLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "RightLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "RightLowerLeg2")
        pyrosim.Send_Motor_Neuron(name = 8, jointName = "Torso_BackLeg1")
        pyrosim.Send_Motor_Neuron(name = 9, jointName = "Torso_BackLeg2")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = "Torso_FrontLeg1")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_LeftLeg1")
        pyrosim.Send_Motor_Neuron(name = 13, jointName = "Torso_LeftLeg2")
        pyrosim.Send_Motor_Neuron(name = 14, jointName = "Torso_RightLeg1")
        pyrosim.Send_Motor_Neuron(name = 15, jointName = "Torso_RightLeg2")
        pyrosim.Send_Motor_Neuron(name = 16, jointName = "BackLeg1_BackLowerLeg1")
        pyrosim.Send_Motor_Neuron(name = 17, jointName = "BackLeg2_BackLowerLeg2")
        pyrosim.Send_Motor_Neuron(name = 18, jointName = "FrontLeg1_FrontLowerLeg1")
        pyrosim.Send_Motor_Neuron(name = 19, jointName = "FrontLeg2_FrontLowerLeg2")
        pyrosim.Send_Motor_Neuron(name = 20, jointName = "LeftLeg1_LeftLowerLeg1")
        pyrosim.Send_Motor_Neuron(name = 21, jointName = "LeftLeg2_LeftLowerLeg2")
        pyrosim.Send_Motor_Neuron(name = 22, jointName = "RightLeg1_RightLowerLeg1")
        pyrosim.Send_Motor_Neuron(name = 23, jointName = "RightLeg2_RightLowerLeg2")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, 
                weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myId = id