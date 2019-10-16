import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x, y)
plt.bar(x, y, color="#e4e4e4")
plt.title("crescimento", color="#ff9900")
plt.xlabel("ano", color="green")
plt.ylabel("população x100.000.000")

plt.show()
