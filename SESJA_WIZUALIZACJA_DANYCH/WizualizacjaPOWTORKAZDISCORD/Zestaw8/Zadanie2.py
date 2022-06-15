xlsx = pd.ExcelFile("ceny22.xlsx")
data = pd.read_excel(xlsx, header=0)

bula = data[data["Rodzaje towarów"]=="bułka pszenna - za 50g"]
chleb = data[data["Rodzaje towarów"]=="chleb pszenno-żytni - za 0,5kg"]

plt.scatter(data["Rok"].unique(), bula["Wartość"].values, color="g", label="Bułka", marker='x')
plt.scatter(data["Rok"].unique(), chleb["Wartość"].values, color="m", label="Chleb", marker='4')
plt.legend(loc='center right')
plt.grid(color="lightsteelblue")
plt.title("Buła i Chleb", size=18)
plt.figtext(0.02, 0.925, "Nr indeksu", size=12, color="tab:brown", rotation=0)
plt.savefig("BulaChleb_wykres.png")
plt.show()
