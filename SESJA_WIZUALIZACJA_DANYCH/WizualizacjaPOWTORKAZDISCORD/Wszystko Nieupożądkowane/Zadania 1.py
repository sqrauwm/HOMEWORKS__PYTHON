import numpy as np
from matplotlib import pyplot as plt

#ZADANIA 1
#ZESTAW 1 wykres słupkowy horyzontalny

x = ["A", "B", "C", "D", "E"]
y1 = [35, 44, 14, 42, 41]
y2 = [-30, -32, -36, -33, -31]

fig, axs = plt.subplots(1, 2, )
axs[0].barh(x, y1, color=["lightblue","pink","tab:orange","tab:gray","tab:purple"])
axs[0].set_title("Wykres lewy")
axs[1].barh(x, y2, color=["tab:pink","tab:cyan","tab:cyan","tab:brown","tab:olive"])
axs[1].set_title("Wykres prawy")
plt.savefig("Z1Z1.png")
plt.show()

#ZESTAW 11 wykres 3 funkcji na przedziale zapis do png

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
plt.savefig("Z1Z11.png")
plt.show()

#ZESTAW 4 wykres 3 funkcji na przedziale zapis do pdf
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
plt.savefig("Z1Z4.pdf", format="pdf")
plt.show()

#ZESTAW 41 wykres 3 funkcji na przedziale zapis do PNG
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
plt.savefig("Z1Z41.png")
plt.show()

#ZESTAW 21 - ZERÓWKA Dwa wykresy kołowe 6 miesięcy procentowo
x = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']

y1 = [15.3, 14.8, 20.5, 18.3, 17.9, 13.1]
colors1 = [(0, 0.75, 0), (0, 0, 0.75), 'pink', (0.75, 0, 1), (0, 0.75, 0), (0.25, 0.5, 1)]
explode1 = [0, 0, 0, 0, 0, 0.05]


y2 = [24.1, 24.1, 22.0, 13.6, 5.8, 10.5]
explode2 = [0, 0, 0.05, 0.05, 0.05, 0.05]
colors2 = [(0.4, 0.4, 0.4), (1, 0.5, 0), (0.25, 0.5, 1), (1, 0.25, 0.25), (0.8, 0.75, 0), (0, 1, 0)]

fig, axs = plt.subplots(1, 2)
axs[0].pie(y1, labels=x, autopct='%.1f %%', explode=explode1, colors=colors1, startangle=30)
axs[0].set_title('Wersja A')


axs[1].pie(y2, labels=x, autopct='%.1f %%', explode=explode2, colors=colors2, startangle=45)
axs[1].set_title('Wersja B')

plt.savefig('Z1Z21-0.png')
plt.show()