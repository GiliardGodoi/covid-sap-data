#%%

from datetime import datetime
from os import path

import pandas as pd
import seaborn as sns
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator


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

frame['NOVOS_CASOS'] = frame['CONFIRMADOS'].diff(periods=1)
frame['RECUPERADOS_DIA'] = frame['RECUPERADOS'].diff(periods=1)
frame['DESCARTADOS_DIA'] = frame['DESCARTADOS'].diff(periods=1)

#%%
plt.figure()
ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'CONFIRMADOS']],
            palette="tab10"
            )

_ = ax.set_title("SAP - COVID-19 - Evolução dos casos")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.grid(False)
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '01-evolucao-casos.png'))


#%%
plt.figure()
ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'ATIVOS']],
            palette="tab10"
            )

_ = ax.set_title("SAP - COVID-19 - Relação entre casos ativos e em investivação")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.grid(False)
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '02-casos-ativos-e-investigacao.png'))

#%%
plt.figure()
ax = sns.lineplot(data=frame[['ATIVOS']], legend=False)
_ = ax.set_title("SAP COVID-19 - Evolução dos casos ativos")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.grid()
# ax.set_ylim([-10, 300])
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '03-evolucao-casos-ativos.png'))


# %%
plt.figure()
ax = sns.lineplot(data=frame[['HOSPITAL']],
             palette="tab10",
             legend=False
            )
_ = ax.set_title("SAP COVID-19 - Evolução dos casos hospitalizados")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
# ax.set_ylim([-10, 250])
ax.xaxis.grid()
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '04-evolucao-hospitalizados.png'))



# %%
plt.figure()
ax = sns.lineplot(data=frame[['CONFIRMADOS','RECUPERADOS']],
             palette="tab10"
            )
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
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
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
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
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.grid()
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '07-media-movel.png'))


# %%

fig = sns.relplot(kind="line", data=frame['OBITOS'], height=5, aspect=2)
ax = fig.facet_axis(0,0)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
# ax.set(yticks=range(4,20))
sns.despine(left=True)
_ = fig.set(title="Evolução da quantidade de óbitos")
plt.tight_layout()
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
ax.xaxis.grid(False)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xticklabels(labels)
ax.set_xlabel("Meses")
ax.tick_params(axis="x", rotation=0)
sns.despine(left=True)
plt.savefig(path.join(outputfolder, '09-evolucao-obitos-por-mes.png'))

# %%

df = frame.resample('W-MON').sum()

df2 = df['2020-11':]

loc = MultipleLocator(base=3.0)

labels = [date.strftime("%d/%m %a") for date in df2.index]

plt.figure(figsize=(15, 7))
ax = plt.subplot()
plt.bar(labels, df2['NOVOS_CASOS'], color='steelblue', label='Novos casos')
plt.bar(labels, df2['RECUPERADOS_DIA'], color='orange', alpha=0.8, label='Recuperados por dia')
ax.yaxis.grid(True)
ax.xaxis.set_major_locator(loc)
ax.xaxis.grid(False)
ax.set(title="Evolução de casos e recuperação por semana")
plt.legend()
plt.xticks(rotation=40)
sns.despine(left=True)

plt.savefig(path.join(outputfolder, '10-relacao-novos-casos-recuperados-semanal.png'))