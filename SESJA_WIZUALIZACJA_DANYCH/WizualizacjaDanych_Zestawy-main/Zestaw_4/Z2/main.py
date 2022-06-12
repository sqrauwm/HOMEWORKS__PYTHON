import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile("kina4.xlsx")
data = pd.read_excel(xlsx, header=0)

miejskie = data[data["Gestor"] == "miejskie"]
powiatowe = data[data["Gestor"] == "powiatowe"]
wojewodzkie = data[data["Gestor"] == "wojewódzkie"]

miejskie_sale = miejskie[miejskie["Wykaz"] == "sale"]
powiatowe_sale = powiatowe[powiatowe["Wykaz"] == "sale"]
wojewodzkie_sale = wojewodzkie[wojewodzkie["Wykaz"] == "sale"]

miejskie_miejsca = miejskie[miejskie["Wykaz"] == "miejsca na widowni"]
powiatowe_miejsca = powiatowe[powiatowe["Wykaz"] == "miejsca na widowni"]
wojewodzkie_miejsca = wojewodzkie[wojewodzkie["Wykaz"] == "miejsca na widowni"]

fig, axs = plt.subplots(1, 2, )
print(miejskie_sale)
axs[0].grid(zorder=0)
axs[0].bar(data["Rok"].unique()-0.3, miejskie_sale["Wartosc"].values,width=0.3, color="tab:green", label="miejskie", zorder=3)
axs[0].bar(data["Rok"].unique(), powiatowe_sale["Wartosc"].values,width=0.3, color="tab:blue", label="powiatowe", zorder=3)
axs[0].bar(data["Rok"].unique()+0.3, wojewodzkie_sale["Wartosc"].values,width=0.3, color="tab:orange", label="wojewódzkie", zorder=3)
axs[0].set_xticks([2015, 2016, 2017])
axs[0].set_yticks(np.arange(0,700,50))
axs[0].set_title("Liczba sal kinowych")
axs[1].grid()
axs[1].bar(data["Rok"].unique()-0.3, miejskie_miejsca["Wartosc"].values,width=0.3, color="tab:green", label="miejskie", zorder=3)
axs[1].bar(data["Rok"].unique(), powiatowe_miejsca["Wartosc"].values,width=0.3, color="tab:blue", label="powiatowe", zorder=3)
axs[1].bar(data["Rok"].unique()+0.30, wojewodzkie_miejsca["Wartosc"].values,width=0.3, color="tab:orange", label="wojewódzkie", zorder=3)
axs[1].set_xticks([2015, 2016, 2017])
axs[1].set_yticks(np.arange(0,150000,10000))
axs[1].set_title("Liczba miejsc w salach kinowych")
axs[0].legend(loc=5)
axs[1].legend(loc=5)
axs[0].set_xlabel("Rok")
axs[1].set_xlabel("Rok")
plt.tight_layout()
plt.savefig("wykres2.png")
plt.show()