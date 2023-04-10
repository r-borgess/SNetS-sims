import matplotlib.pyplot as plt

x = [3640, 5460, 7280, 9100]

y = [ 0.2833713209790903, 0.39713606183728073, 0.4511941333861857, 0.5022792587454167]


plt.plot(x, y, linestyle = 'dashed', marker = 'o', markerfacecolor = 'red')


plt.xlabel('Carga (Erlangs)')

plt.ylabel('Probabilidade de Bloqueio')
plt.show()