#%%
import os
from os import path
from datetime import datetime
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = (10, 5)
params = {
    'axes.facecolor' : 'white',
    'axes.titlesize' : 'larger',
    'axes.titleweight' : 'bold',
    'axes.edgecolor': 'gray',
    "axes.grid" : True,
    "grid.linewidth": 0.9,
    'grid.linestyle': '--',
    'axes.grid.which' : 'major'
    }

sns.set_style("whitegrid", params)


inputfile = path.join('..', 'data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx')
outputfolder = path.join('..', 'data', 'charts')

assert path.exists(inputfile), f"Caminho para o arquivo não existe:\n{inputfile}"
assert path.exists(outputfolder), f"Caminho para o arquivo não existe:\n{outputfolder}"

frame = pd.read_excel(inputfile,
                   index_col="DATA",
                   parse_dates=['DATA'],
                   engine='openpyxl')

#%%
plt.figure()
ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'CONFIRMADOS']],
            palette="tab10"
            )

_ = ax.set_title("SAP - COVID-19 - Evolução dos casos")
ax.xaxis.grid(False)
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '01-evolucao-casos.png'))


#%%
plt.figure()
ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'ATIVOS']],
            palette="tab10"
            )

_ = ax.set_title("SAP - COVID-19 - Relação entre casos ativos e em investivação")

ax.xaxis.grid(False)
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '02-casos-ativos-e-investigacao.png'))

#%%
plt.figure()
ax = sns.lineplot(data=frame[['ATIVOS']], legend=False)
_ = ax.set_title("SAP COVID-19 - Evolução dos casos ativos")

ax.xaxis.grid()
ax.set_ylim([-10, 300])
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '03-evolucao-casos-ativos.png'))


# %%
plt.figure()
ax = sns.lineplot(data=frame[['HOSPITAL']],
             palette="tab10",
             legend=False
            )
_ = ax.set_title("SAP COVID-19 - Evolução dos casos hospitalizados")

# ax.set_ylim([-10, 250])
ax.xaxis.grid()
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '04-evolucao-hospitalizados.png'))



# %%
plt.figure()
ax = sns.lineplot(data=frame[['CONFIRMADOS','RECUPERADOS']],
             palette="tab10"
            )
_ = ax.set_title("Santo Antônio da Platina - COVID-19")
ax.xaxis.grid()
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '05-relacao-confirmados-recuperados.png'))

# %%
plt.figure()
ax = sns.lineplot(data=frame[['ATIVOS','EM INVESTIGACAO']],
             palette="tab10"
            )
_ = ax.set_title("Santo Antônio da Platina - COVID-19")
# ax.set_ylim([-10, 300])
ax.xaxis.grid()
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '06-relacao-ativos-investigacao.png'))

# %%
plt.figure()

dias = 7

ax = frame['ATIVOS'].plot()
ax = frame['ATIVOS'].rolling(dias).mean().plot()


_ = ax.set_title(f"SAP - Covid-19 - Média Móvel {dias} dias")
ax.xaxis.grid()
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '07-media-movel.png'))


# %%
plt.figure()
ax = sns.relplot(kind="line", data=frame['OBITOS'], height=5, aspect=2)

# ax.set(yticks=range(4,20))

_ = ax.set(title="Evolução da quantidade de óbitos")
plt.savefig(path.join(outputfolder, '08-evolucao-obitos.png'))


# %%
plt.figure()
deaths = frame['OBITOS'].diff(periods=1)

groupdeaths = deaths.groupby([(deaths.index.year),(deaths.index.month)]).sum()

def formatter(label):
    yearDict = {
        2020 : '20',
        2021 : '21'
    }
    monthDict = {
        1:'Jan',
        2:'Fev',
        3:'Mar',
        4:'Abr',
        5:'Maio',
        6:'Jun',
        7:'Jul',
        8:'Ago',
        9:'Set',
        10:'Out',
        11:'Nov',
        12:'Dez'}

    return f"{monthDict[label[1]]} {yearDict[label[0]]}"

# formatter((2020, 7))

labels = [formatter(label) for label in groupdeaths.index]

# labels

ax = groupdeaths.plot(kind='bar', color='steelblue')

ax.set(title='SAP COVID-19 - Total de mortes por mês')
ax.set_xticklabels(labels)
ax.set_xlabel("Meses")
ax.tick_params(axis="x", rotation=0)
sns.despine(left=True)

plt.savefig(path.join(outputfolder, '09-evolucao-obitos-por-mes.png'))
