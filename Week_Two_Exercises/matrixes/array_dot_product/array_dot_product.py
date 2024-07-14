import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

v = np.array([2.0, 2.0, 4.0])
print(v.shape)

plot = plt.axes(projection="3d")
plot.plot3D(5, 5, 5)
plt.title("array dot product")
plot.set_xlabel("e0")
plot.set_ylabel("e1")
plot.set_zlabel("e2")
plt.quiver(0, 0, 0, v[0], v[1], v[2])
plt.show()
