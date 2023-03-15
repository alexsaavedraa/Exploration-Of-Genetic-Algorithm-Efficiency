import os
import matplotlib.pyplot as plt
import random

#os.system("python3 search.py ")

from parallelHillCilmber import PARALLEL_HILL_CLIMBER
evolutions = []
for i in range(3):
      random.seed(i+1)
      phc = PARALLEL_HILL_CLIMBER() 
      #input("Start ")
      phc.Evolve()
      #Wait for input
      #input("Show ")
   # phc.Show_Best()
      phc.save_best()
      #phc.Save_data()
      evolutions.append(phc.bestOfGens)
      new_filename = str(i) + "_alldata.csv"
      os.system(f'copy alldatas.csv results\\{new_filename}')
      os.system('del alldatas.csv')



print("Done")

for e in evolutions:
      plt.plot(e)
#plt.legend()
plt.show()