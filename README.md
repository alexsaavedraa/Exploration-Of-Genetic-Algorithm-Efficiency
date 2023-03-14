# Exploration-Of-Genetic-Algorithm-Efficiency
## Workup: Environment, Bots, and Evolution
If you are interested only in the results, skip to the results section. Otherwise, We start from Here:
### Environment
First we Create the ground plane:
![image](https://user-images.githubusercontent.com/114758213/225104782-9eb18c2e-e8cd-4e69-9ef9-320348bd6ae4.png)
![image](https://user-images.githubusercontent.com/114758213/225107083-899d8bf3-91a5-4294-b226-caf0c42d1eb7.png)

We Add Gravity, Collisions, and a Friction. We also add a box to show that our physics are working corectly
## Gravity:
![ezgif-3-fdca56c21b](https://user-images.githubusercontent.com/114758213/225111210-9561f579-9f80-4f42-ad5b-8ab2ad2e9e45.gif)

## When the block is moved, it comes to a stop due to the bullet physics engine's friction:
![Friction](https://user-images.githubusercontent.com/114758213/225111692-1fa9526b-4af2-4de4-a4b1-21bebe399365.gif)


# Bots!

## A Bot is made from these cube shaped blocks. 
They can be any shape, but for demonstration purposes, they will be made of cubes:
![image](https://user-images.githubusercontent.com/114758213/225113095-1ad50df8-42bf-4c96-95ec-df0d769fed91.png)
## One cube is a bot. So is Two cubes:
![image](https://user-images.githubusercontent.com/114758213/225113628-b9aa0867-c72e-467a-b2a1-b4c40bb898bd.png)
## Bot Parts are connected by Joints. The parts of the bot can rotate around the joint by a set number of degrees. In our simulations, it will be between 0 and 90. 
![image](https://user-images.githubusercontent.com/114758213/225115743-5b5c2685-337c-495a-8b6e-e31fb40048b0.png)
## Next we add motors. Motors allow our bot to move.

![Motors](https://user-images.githubusercontent.com/114758213/225117052-a06a4c13-f67e-402e-bab5-f51facd33658.gif)


## Our bots have two different kinds of blocks, sensor blocks and regular blocks. Sensor Blocks can sense their angle.
![image](https://user-images.githubusercontent.com/114758213/225119845-b03fd5d2-a8aa-4463-a2a9-586092ab5e89.png)

## Neurons Can be mapped directly from sensors to motor joints
![image](https://user-images.githubusercontent.com/114758213/225119590-9be3ae82-259e-4d36-9fef-f3d2998853bf.png)

## Or they can pass through a hidden layer
![image](https://user-images.githubusercontent.com/114758213/225120331-669dc04b-bfd8-48de-921c-10b80fe61bb8.png)

## With many parts, all sensors and all neurons become connected, creating a brain:
![image](https://user-images.githubusercontent.com/114758213/225121470-510e3bbd-e9e0-46c9-9975-cb5a5a198180.png)

## Brain Training:
Before Training, bots will have the weights of each neuron be random, but through the process of training, the weights will adjust to produce higher fitness values
![image](https://user-images.githubusercontent.com/114758213/225135012-78d91bd3-71e5-4385-8cd7-71450e274bac.png)
![image](https://user-images.githubusercontent.com/114758213/225135367-6a77a6b8-8c4a-4661-b3b3-875c12c857ba.png)

## Here Is What Random Brains Look Like
![random Brains](https://user-images.githubusercontent.com/114758213/225137190-1c421c2d-c91c-44e3-b84d-4d26f6368019.gif)
## Here Is what an Evolved Brain Looks Like
![Evolved Brain](https://user-images.githubusercontent.com/114758213/225139030-1c3c13dd-eb22-464d-a6f9-b7454c3624dd.gif)


# Generating a Body
![image](https://user-images.githubusercontent.com/114758213/225142965-f2220ec9-9228-4eb7-b11b-d9861c744735.png)
![image](https://user-images.githubusercontent.com/114758213/225144189-e88f3b35-a079-490d-84c2-384b67466e04.png)

## Adding A Part
![image](https://user-images.githubusercontent.com/114758213/225147786-8d72e50f-5e5d-49e7-8a56-6e64ab2798f9.png)
This same process is continued no matter how many parts are already added. 

## Here is a Robot with 12 parts made in this way
![image](https://user-images.githubusercontent.com/114758213/225151237-0ae720bc-1907-4a08-83cf-05ea8f71f009.png)

## What is Mutation, and Evolution?
![image](https://user-images.githubusercontent.com/114758213/225155260-b625260e-f3e1-4454-a0f2-c54c578709e7.png)
A mutation is the process of adding between 1 and 5 parts, in the same way shown above, or changing the weight of one or more of the neurons in a brain.
The fitness of the parent is measured against the fitness of the child. The ratio of parents to children kept is related to the fitness of each. The higher the fitness of an individual, the more likely it will be kept as part of the next generation
As you can see in the diagram, evolution does not always entail adding more parts. Sometimes, parts may even be removed

##Phenotypes and GenoTypes:
A phenotype is how a robot looks. The genotype is how a robot is stored or encoded. For this simulation, a direct encoding was used, meaning  each robot is stored as a list of parts and what other parts they are attatched to. the brain is stored as a list of neurons, their synapses, and their weights. In the future it may be interesting to explore the consequences of an indirect encoding. Here we can see the encoding of a body and brain in plaintext:
![image](https://user-images.githubusercontent.com/114758213/225157125-9381ce6a-a841-4fc7-a6b4-b94e4dd8adeb.png)





