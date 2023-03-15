import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
from sensor import SENSOR
from motor import MOTOR
import constants as c
import math
import random




class ROBOT:
      def __init__(self, solutionID, test, evolved):
            self.sensors = {}
            self.motors = {}
            

            if test:
                  if evolved:
                        self.nn = NEURAL_NETWORK(f'results/evolved/{solutionID}/brain{solutionID}.nndf')
                        self.robotId = p.loadURDF(f'results/evolved/{solutionID}/body{solutionID}.urdf') 
                  else:
                        self.nn = NEURAL_NETWORK(f'results/random/{solutionID}/brain{solutionID}.nndf')
                        self.robotId = p.loadURDF(f'results/random/{solutionID}/body{solutionID}.urdf') 
            else:
                  self.nn = NEURAL_NETWORK(f'brain{solutionID}.nndf')
                  self.robotId = p.loadURDF(f'body{solutionID}.urdf') 

            if not test:
                  os.system(f'del brain{solutionID}.nndf')
                  os.system(f'del body{solutionID}.urdf')
            self.solutionID = solutionID
            #self.totalHeight = 0
            self.totalStandReward = 0
            self.lastSpot = 0
            #self.moveReward = 0
            self.lastYUp = 0
      
      def Prepare_To_Sense(self):
            for linkName in pyrosim.linkNamesToIndices:
                  self.sensors[linkName] = SENSOR(linkName)
      
      def Sense(self, i):
            for linkName in self.sensors:
                  self.sensors[linkName].Get_Value(i)
      
      def Prepare_To_Act(self):
            for jointName in pyrosim.jointNamesToIndices:
                  self.motors[jointName.decode('utf-8')] = MOTOR(jointName)
      
      def Act(self, i):
            for neuronName in self.nn.Get_Neuron_Names():
                  if self.nn.Is_Motor_Neuron(neuronName):
                        jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                        desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                        self.motors[jointName].Set_Value(self.robotId, desiredAngle)
      
      def Think(self):
            self.nn.Update()
            #self.nn.Print()
      
      def Get_Fitness(self):
            
            basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
            basePosition = basePositionAndOrientation[0]
            xPosition = basePosition[0]
            yPosition = basePosition[1]
            zPosition = basePosition[2]

            fitness = yPosition * 10
            ###
            #fitness = self.solutionID
            ###

            f = open(f'tmp{self.solutionID}.txt', "w")
            f.write(str(fitness))
            f.close()
            os.system(f'move tmp{self.solutionID}.txt fitness{self.solutionID}.txt')

  
            






