from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

#auxiliares
debug = True
i = 0

#quantidade de nós na topologia
n = 14
combinatoria = (n*(n-1))

#qtd de pontos de carga e replicações
loadPoints = 4
replications = 10

#taxa de chegada
arrivalRate = 16.48351648351648

#incremento entre pontos
inc = 1.098901098901099

randomFitData = {
	'carga' : ['3000', '3200', '3400', '3600'],
	'prob': ['0.120', '0.139', '0.156', '0.173'],
	'spec' : ['1.78', '1.82', '1.87', '1.92']
}

rf = pd.DataFrame(randomFitData)
print(rf)

#probabilidades em cada replicação de cada ponto de carga
reps1 = [0.11954243277235431,0.12106965323111936,0.11919306861512048,0.11854424946597193,0.1171867201692919,0.12092990756822583,0.12148889021979996,0.12185821804316145,0.1198718332634605,0.12447345830588329]
reps2 = [0.135992493661536,0.13982551755804437,0.13853786109281108,0.13146074145055997,0.14047433670719292,0.14208141183046855,0.1422311393264259,0.13856780659200255,0.14330917729731887,0.14142261084825616]
reps3 = [0.1583917270567567,0.16237447844922243,0.15217304505799445,0.1550378311473119,0.15819209039548024,0.15218302689105828,0.16044798466790441,0.16062765766305323,0.15351061068854685,0.15410952067237627]
reps4 = [0.17757681020542612,0.17429278712742807,0.17888443033678705,0.17348425864925834,0.17083907288734504,0.17027010840270707,0.16893254277215466,0.17151783753568506,0.16974107125032442,0.17761673753768142]

#utilização de espectro em cada replicação de cada ponto de carga
spec1 = [1.782603242354615,1.7739906339212452,1.790989727531148,1.7745532831950321,1.7904675188599892,1.777550399466156,1.7782951073080795,1.7970159310055958,1.785587295043459,1.7756066147112248]
spec2 = [1.8439611455446703,1.8265434863094399,1.8446435278985467,1.8360934455824125,1.8327429447723471,1.8183274508576235,1.813241606242518,1.8128422102739021,1.8210066032094212,1.8278379152499067]
spec3 = [1.8741113694382892,1.8635407563915916,1.883412223134588,1.8718622455142886,1.875372563411884,1.8794868814609478,1.8698588526268658,1.8692719527448867,1.8745530485369057,1.8854700999578522]
spec4 = [1.9109804112481197,1.9100409435225822,1.8997637325635575,1.9142847049619842,1.9394042338682589,1.925442552508998,1.9261342098857261,1.9279123940450957,1.9331580621280693,1.9039135818264887]

#estruturas de dados
carga = [0 for x in range(loadPoints)]
prob = [0 for x in range(loadPoints)]
specUtil = [0 for x in range(loadPoints)]
reps = np.array([reps1, reps2, reps3, reps4])
spec = np.array([spec1, spec2, spec3, spec4])

#preenchendo o vetor de pontos de carga e calculando as médias de prob de bloqueio e utlização de rede
while(i < loadPoints):
	if debug == True:
		print(i)
	carga[i] = combinatoria * (arrivalRate + i*inc)
	prob[i] = mean(reps[i])
	specUtil[i] = mean(spec[i])
	i += 1

#auxiliar
if debug == True:
	print(carga)
	print(prob)
	print(specUtil)

#parametros dos graficos
lineColorFF = 'red'
pointColorFF = 'red'
lineColorLF = 'green'
pointColorLF = 'green'
lineColorRF = 'blue'
pointColorRF = 'blue'
lineWidth = 1.0
lineStyle = '--'
point = 'o'

sns.lineplot(
    data=rf, x="carga", y="prob", err_style="bars", errorbar=("se", 2),
)
plt.show()
'''
#plotando o gráfico de probabilidade de bloqueio em função da carga
plt.plot(carga, prob, color= lineColorRF, linewidth = lineWidth, linestyle = lineStyle, marker=point, markerfacecolor=pointColorRF)

plt.xlabel('Carga (Erlangs)')
plt.ylabel('Probabilidade de bloqueio')

plt.title('Evolução da probabilidade de bloqueio em função da carga')

plt.show()

#plotando o gráfico de utilização de espectro em função da carga
plt.plot(carga, specUtil, color= lineColorRF, linewidth = lineWidth, linestyle = lineStyle, marker=point, markerfacecolor=pointColorRF)

plt.xlabel('Carga (Erlangs)')
plt.ylabel('Utilização de Espectro')

plt.title('Utilização da rede em função da carga')

plt.show()
'''