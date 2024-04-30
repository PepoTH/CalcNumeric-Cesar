import numpy as np

a = np.arange(6)
a2 = a[np.newaxis, :]
a2.shape

print(a[0])