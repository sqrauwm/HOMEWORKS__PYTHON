import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image

xlsx = pd.ExcelFile("turystyka11.xlsx")
data = pd.read_excel(xlsx, header=None)

data = data.transpose()

r2014 = data[data[1] == '2014']
r2019 = data[data[1] == '2019']
print(r2014)
fig, axs = plt.subplots(1, 2, )
axs[0].pie(r2014[2].values, labels=['5*', '4*', '3*', '2*', '1*'], autopct='(%.f %%)', pctdistance=1.55)
axs[0].set_title("Rok 2014")
axs[1].pie(r2019[2].values, labels=['5*', '4*', '3*', '2*', '1*'], autopct='(%.f %%)', pctdistance=1.55)
axs[1].set_title("Rok 2019")
plt.tight_layout()
plt.savefig("wykres3.png")
im = Image.open("wykres3.png")
im = im.convert("RGB")
im.save("wykres3.jpg")
plt.show()