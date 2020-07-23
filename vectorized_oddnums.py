import numpy as np
from datetime import datetime

# Odd numbers without Numpy.
'''
for n in range(1, 50):
    
    if n % 2 == 1:
        print(n, "is Odd.")
    else:
        continue

## Time Process: 0:00:00.007981
'''

# Odd numbers with Numpy's vectorization.
start = datetime.now()

n = np.arange(1, 50, 2)
print(n, "is Odd.")

end = datetime.now()
print("\nTime Process: {}".format(end - start))