import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = np.arange(-5, 5.1, 0.1)
y1 = -1 * x**3 + 3 * x - 7
y2 = 4 * x + 6
y3 = 6 + 4 * x**3
plt.plot(x, y1, label="$-x^3 + 3x - 7$", color='c', ls='dotted')
plt.plot(x, y2, label="$4x+6$", color='m', ls="dashdot")
plt.plot(x, y3, label="$6 + 4x^3$", color='y', ls="dashed")
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Wykresy funkcji w przedziale $[-5; 5]$")
plt.legend()
plt.savefig("wykres1.pdf", format="pdf")
plt.show()
