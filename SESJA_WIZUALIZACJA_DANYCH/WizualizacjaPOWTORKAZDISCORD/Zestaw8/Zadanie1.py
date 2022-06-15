wybuch = [0, 0.1, 0 , 0 ,0 ,0 ]
kolorki = ["tab:brown", "tab:pink", "tan", "lawngreen", "tab:brown", "tab:blue"]
plt.subplot(2, 2, 3)
x1 = ["A", "B", "C", "D", "E", "F"]
y1 = [20.4, 17.6, 9.7, 19.9, 15.7, 16.7]
plt.pie(y1, labels=x1, autopct='%.1f %%', startangle=35, radius=1.2, explode=wybuch, colors=kolorki)
plt.title("Lewo Dół")


plt.subplot(2, 2, 2)
y2 = [15.7, 25.6, 16.9, 21.5, 12.8, 7.6]
plt.pie(y2, labels=x1, autopct='%.1f %%', startangle=42, radius=1.2 , explode=wybuch, colors=kolorki)
plt.title("Prawo Góra")

plt.suptitle("LEWY PRAWY")

plt.savefig("wykresior3232.png")
im = Image.open("wykresior3232.png")
im = im.convert("RGB")
im.save("SUPERWYKRES.jpg")

plt.show()
