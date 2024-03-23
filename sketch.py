import numpy as np
import matplotlib.pyplot as plt


X = np.arange(-4.5, 7.4, 1 / 120)
Y = np.arange(-5.2, 3.3, 1 / 120)
Z = np.zeros((len(X), len(Y), 3))


for xi, x in enumerate(X):
    for yi, y in enumerate(Y):
        z = complex(x, y)
        for i in range(1, 12):
            if abs(z) < 1.1 and abs(z) > 0.9:
                if i == 1:
                    color = (1, 0.7, 0)
                elif i < 3:
                    color = (1, 1, 0)
                elif i < 5:
                    color = (0, 1, 0)
                elif i < 7:
                    color = (0, 0, 1)
                elif i < 9:
                    color = (0.5, 0, 0.5)
                elif i < 11:
                    color = (1, 0, 1)
                else:
                    color = (1, 0, 0)
                Z[xi, yi] = color
            z = ((1 - i) * (z**4) + (7 + i) * z) / (2 * (z**3) + 6)


plt.imshow(Z, extent=(X.min(), X.max(), Y.min(), Y.max()))
plt.axis("off")
plt.show()
