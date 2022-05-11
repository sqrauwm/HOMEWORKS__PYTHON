import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# Zadanie 1, 2

x = np.arange(1, 20, 1)
plt.axis([0, 20, 0, 1])
plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x)=1/x dla x [1, 20]')
plt.legend()
plt.show()

# Zadanie 3

x = np.arange(0, 31, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.xlabel('x')
plt.ylabel('Wartości')
plt.title("Wykres sin(x) oraz cos(x)")
plt.legend()
plt.show()
# Zadanie 4
