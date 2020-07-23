import numpy as np
from datetime import datetime

# Dot product without Numpy.

## NOTE: This code has no comments bc it's a past file that I already uploaded in an Unit 1 assignment.
'''
a_matrix =  [[1,2], [3,-2], [0,1]]

b_matrix =  [[-3,-1,2], [5,2,-1]]

ab_matrix = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(a_matrix)):
   for j in range(len(b_matrix[0])):
       for k in range(len(b_matrix)):

           ab_matrix[i][j] += a_matrix[i][k] *  b_matrix[k][j]

   print(result)
  

## Time Process: 0:00:00.000631
'''

# Dot product with Numpy's vectorization
start = datetime.now()

a_matrix = [[1,2], [3,-2], [0,1]]  
b_matrix = [[-3,-1,2], [5,2,-1]]  

ab_matrix = np.dot(a_matrix, b_matrix)
print(ab_matrix)

end = datetime.now()

print("\nTime Process: {}".format(end - start))