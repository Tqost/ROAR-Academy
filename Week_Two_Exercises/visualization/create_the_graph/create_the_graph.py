import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(1.0, 2.1, 0.1)
y1 = x1 * 2
x2 = np.arange(2.0, 3.1, 0.1)
y2 = x2 * -3 + 10
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
plt.xticks([1.0, 1.5, 2.0, 2.5, 3.0], ["1.0", "1.5", "2.0", "2.5", "3.0"])
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.plot(x1, y1, color="blue")
plt.plot(x2, y2, color="blue")
axes.spines["left"].set_position(("data", 1.0))
axes.spines["bottom"].set_position(("data", 1.0))
axes.spines["top"].set_position(("data", 4.0))
axes.spines["right"].set_position(("data", 3.0))
plt.title("Sample graph!")
plt.xlim((1.0, 3.0))
plt.ylim((1.0, 4.0))
plt.show()
