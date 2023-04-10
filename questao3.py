import matplotlib.pyplot as plt

x = [20000, 40000, 60000, 80000, 100000, 120000]

y = [ 0.021702507184619958, 0.027524762331392165, 0.025738592934764548, 0.03029358210072086, 0.031002456772243576 ,0.031144430946397964]


plt.plot(x, y, linestyle = 'dashed', marker = 'o', markerfacecolor = 'red')


plt.xlabel('Requisições')

plt.ylabel('Probabilidade de Bloqueio')
plt.show()