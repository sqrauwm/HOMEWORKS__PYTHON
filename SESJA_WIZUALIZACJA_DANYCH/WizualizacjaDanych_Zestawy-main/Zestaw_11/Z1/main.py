import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 3*np.pi+0.1, 0.1)
y1 = np.sin(2 * x)
y2 = 3 * x - 5
y3 = 2 * np.cos(x)

plt.plot(x, y1, label="$\sin 2x$", color='c', ls='dotted')
plt.plot(x, y2, label="$3x - 5$", color='m', ls='dashed')
plt.plot(x, y3, label="$2 \cos x$", color='y', ls='dashdot')
plt.xticks(np.arange(0, 11, 1))
plt.title("Wykresy funkcji w przedziale $[0; 3\pi]$")
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.xlim(0, 3*np.pi+0.1)
plt.legend()
plt.savefig("wykres1.png")
plt.show()