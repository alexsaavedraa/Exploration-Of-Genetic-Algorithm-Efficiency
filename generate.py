import pyrosim.pyrosim as pyrosim
import random

def Create_World():
      length = 1
      width = 1
      height = 1

      x = -2
      y = 2
      z = 0.5

      pyrosim.Start_SDF("world.sdf")
      pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
      pyrosim.End()

def Create_Robot():
      Generate_Body()
      Generate_Brain()
      
def Generate_Body():
      length = 1
      width = 1
      height = 1

      x = 0
      y = 0
      z = 0.5
      pyrosim.Start_URDF("body.urdf")

      pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])

      pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5,0,1])
      pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5] , size=[length,width,height])

      pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-0.5,0,1])
      pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5] , size=[length,width,height])


      pyrosim.End()

def Generate_Brain():
      pyrosim.Start_NeuralNetwork("brain.nndf")

      pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
      pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
      pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

      pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
      pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

      '''
      pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -0.5 )
      pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.5 )
      pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 0.0 )

      pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.5 )
      pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = -0.5 )
      '''

      for sensorNeuron in [0,1,2]:
            for motorNeuron in [3,4]:
                  pyrosim.Send_Synapse( sourceNeuronName = sensorNeuron, targetNeuronName = motorNeuron , weight = random.randint(-1.0,1.0) )

      pyrosim.End()
      


Create_World()
Create_Robot()
