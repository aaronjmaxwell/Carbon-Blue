import numpy as np
import matplotlib.pyplot as plt
class Shape(object):
   def __init__(self, t):
      self.X = (1 + np.cos(6 * t) ** 2 + 0.2 * (np.cos(6 * t) * np.cos(24 * t)) ** 10 \
                + (0.25 * np.cos(30 * t) ** 2 + 1 / 9. * np.cos(30 * t) ** 12) \
                * (1 - np.sin(6 * t) ** 10)) * np.sin(2 * t) * (1 - np.cos(t) ** 4) \
                * (1 - np.cos(t) ** 10 * np.cos(3 * t) ** 2) + 1 / 70. * np.cos(t) ** 9
      self.Y = -1.05 * np.cos(2 * t) * (1 - np.cos(t) ** 4 + 0.5 * (np.cos(t) \
                * np.cos(3 * t)) ** 10) * (1 + np.cos(6 * t) ** 2 + 0.2 * (np.cos(6 * t) \
                * np.cos(18 * t)) ** 10 + (0.25 * np.cos(30 * t) ** 4 + 0.1 \
                * np.cos(30 * t) ** 12) * (1 - np.cos(t) ** 10* np.cos(3 * t) ** 2) * (1 \
                - np.sin(6 * t) ** 10))
t = np.linspace(0, np.pi, 1000)
shape = Shape(t)
plt.plot(shape.X, shape.Y)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.savefig('mapleleaf.png', dpi = 300)
plt.clf()
