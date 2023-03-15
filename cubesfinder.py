import numpy as np



array = np.zeros((15, 15, 15))

center = array[7,7,7] = 1


num_cubes = 3
i = 0
import numpy as np



# Loop through every voxel in the array
for z in range(array.shape[0]):
      for y in range(array.shape[1]):
            for x in range(array.shape[2]):
                  # Check if the current voxel is a 1
                  if array[z, y, x] == 1:
                        # Check if the voxel in the positive Z direction is also a 1
                        print(z,x,y)
                        if (z < array.shape[0] - 1) and (array[z+1, y, x] == 1):
                              # There is something adjacent to the current voxel in the positive Z direction
                              # Print the index of z for this voxel
                              print(f"Adjacent voxel in positive Z direction found at ({x}, {y}, {z+1})")
                        else:
                              print("non adjacent voxel found")
