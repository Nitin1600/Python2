import numpy as np
# a = np.array([1,2,3])
# print(a)

# a = np.array([(1,2,3), (4,5,6)])
# print(a)

# a = np.array([1,2,3,4,5], ndmin=2)
# print(a)

# a = np.array([1,2,3,4,5], dtype=complex)
# print(a)

# import numpy as np
# import time
# import sys
# S = range(1000)
# print(sys.getsizeof(5)*len(S))
#
# D = np.arange(1000)
# print(D.size*D.itemsize)

# import time
# import sys
# SIZE = 1000000
#
# L1 = range(SIZE)
# L2 = range(SIZE)
# A1 = np.arange(SIZE)
# A2 = np.arange(SIZE)
#
# start = time.time()
# result = [(x,y) for x,y in zip(L1,L2)]
# print((time.time()-start)*1000)
#
# start = time.time()
# result = A1+A2
# print((time.time()-start)*1000)

# import numpy as np
# a = np.array([(1,2,3),(4,5,6)])
# print(a.ndim)

# import numpy as np
# a = np.array([(1,2,3)])
# print(a.itemsize)
# print(a.dtype)

# import numpy as np
# a = np.array([(1,2,3,4,5,6)])
# print(a.size)
# print(a.shape)

# import numpy as np
# a = np.array([(8,9,10),(11,12,13)])
# print(a)
# a = a.reshape(3,2)
# print(a)

# import numpy as np
# a = np.array([(1,2,3,4), (3,4,5,6), (7,8,9,10)])
# print(a[0,2])
# print(a[0:,2])
# print(a[0:2,1])

# import numpy as np
# a = np.linspace(1,3,10)
# print(a)

# import numpy as np
# a = np.array([(1,2,3)])
# print(a.min())
# print(a.max())
# # print(a.size())
# print(a.sum())
#
# import numpy as np
# a = np.array([(1,2,3), (3,4,5)])
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# import numpy as np
# a = np.array([(1,2,3), (3,4,5)])
# print(np.sqrt(a))
# print(np.std(a))

# import numpy as np
# x = np.array([(1,2,3), (3,4,5)])
# y = np.array([(1,2,3), (3,4,5)])
# # print(x+y)
# # print(x-y)
# # print(x*y)
# # print(x/y)
# print(np.vstack((x,y)))
# print(np.hstack((x,y)))
# print(x.ravel())


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0,3*np.pi,0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0,3*np.pi,0.1)
# y = np.tan(x)
# plt.plot(x,y)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# a = np.array([1,2,3])
# print(np.exp(a))
# print(np.log(a))
# print(np.log10(a))