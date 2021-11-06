import numpy as np

a = np.arange(200)

print(a)
a = a.reshape(4,50)
print(a)


b = np.arange(20)
b2 = b[np.newaxis,:]
print(b2.shape)
