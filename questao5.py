import matplotlib.pyplot as plt

x = [5460, 4550]

y = [ 0.06352195025270042, 0.1144088791992865]


plt.plot(x, y, linestyle = 'dashed', marker = 'o', markerfacecolor = 'red')


plt.xlabel('Carga (Erlangs)')

plt.ylabel('Probabilidade de Bloqueio')
plt.show()