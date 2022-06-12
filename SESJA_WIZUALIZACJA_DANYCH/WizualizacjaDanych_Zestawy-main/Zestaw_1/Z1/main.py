import matplotlib.pyplot as plt

x = ["A", "B", "C", "D", "E"]
y1 = [35, 44, 14, 42, 41]
y2 = [-30, -32, -36, -33, -31]

fig, axs = plt.subplots(1, 2, )
axs[0].barh(x, y1, color=["lightblue","pink","tab:orange","tab:gray","tab:purple"])
axs[0].set_title("Wykres lewy")
axs[1].barh(x, y2, color=["tab:pink","tab:cyan","tab:cyan","tab:brown","tab:olive"])
axs[1].set_title("Wykres prawy")
plt.savefig("wykres1.png")
plt.show()
