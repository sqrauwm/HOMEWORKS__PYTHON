import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0.5, 10.01, 0.01)
y1 = np.log(2*x)
y2 = -4 * x + 2
y3 = 2 * np.cos(x)

plt.plot(x, y1, label="$y=\log 2x$", color='c', ls='dashed')
plt.plot(x, y2, label="$y=-4x+2$", color='m', ls='dotted')
plt.plot(x, y3, label="$y=2\cos x$", color='y', ls='dashdot')
plt.title("Wykres funkcji w przedziale $[0,5; 10]$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.xticks(np.arange(0, 11, 1))
plt.xlim(0.5, 10)
plt.legend()
plt.savefig("wykres1.png")
plt.show()


