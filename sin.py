import numpy as np
import matplotlib.pyplot as plt

x_axis = np.range(0,11,.25)
y_data1 = np.sin(x_axis)
y_data2 = np.cos(x_axis)
plt.plot(x_axis, y_data1,color='black')
plt.plot(x_axis, y_data2,color='green')
plt.show()
