import matplotlib.pyplot as plt

x = [45500, 9100, 3640, 3640]

y = [ 2.217076153879371, 1.8415936286610015, 1.3700243797071605, 1.3548116120575444]


plt.plot(x, y, linestyle = 'dashed', marker = 'o', markerfacecolor = 'red')


plt.xlabel('Carga (Erlangs)')

plt.ylabel('Utilização de Espectro')
plt.show()