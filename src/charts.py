#%%

from os import path

import pandas as pd
import seaborn as sns
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator
import matplotlib.ticker as plticker


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

out = path.join('..', 'data', 'charts')
inputfile = path.join('..', 'data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx')

def read_data(inputfile):
    assert path.exists(inputfile), f"Caminho para o arquivo não existe:\n{inputfile}"

    frame = pd.read_excel(inputfile,
                    index_col="DATA",
                    parse_dates=['DATA'],
                    engine='openpyxl')
    return frame


#%%
def chart01_evolucao_casos(frame, outputfolder=out, filename='01-evolucao-casos.png'):
    plt.figure()
    ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'CONFIRMADOS']],
                palette="tab10"
                )

    _ = ax.set_title("SAP - COVID-19 - Evolução dos casos")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid(False)
    sns.despine(left=True)
    plt.savefig(path.join(outputfolder, filename))


#%%
def chart02_casos_ativos_investigacao(frame, outputfolder=out, filename='02-casos-ativos-e-investigacao.png'):
    plt.figure()
    ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'ATIVOS']],
                palette="tab10"
                )

    _ = ax.set_title("SAP - COVID-19 - Relação entre casos ativos e em investivação")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid(False)
    sns.despine(left=True)
    plt.savefig(path.join(outputfolder, filename))

#%%
def chart03_evolucao_casos_ativos(frame, outputfolder=out, filename='03-evolucao-casos-ativos.png'):
    plt.figure()
    ax = sns.lineplot(data=frame[['ATIVOS']], legend=False)
    _ = ax.set_title("SAP COVID-19 - Evolução dos casos ativos")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid()
    # ax.set_ylim([-10, 300])
    sns.despine(left=True)
    plt.savefig(path.join(outputfolder, filename))


# %%
def chart04_evolucao_hospitalizados(frame, outputfolder=out, filename='04-evolucao-hospitalizados.png'):
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
    plt.savefig(path.join(outputfolder, filename))



# %%
def chart05_relacao_confirmados_recuperados(frame, outputfolder=out, filename='05-relacao-confirmados-recuperados.png'):
    plt.figure()
    ax = sns.lineplot(data=frame[['CONFIRMADOS','RECUPERADOS']],
                palette="tab10"
                )
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    _ = ax.set_title("Santo Antônio da Platina - COVID-19")
    ax.xaxis.grid()
    sns.despine(left=True)
    plt.savefig(path.join(outputfolder, filename))

# %%
def chart06_relacao_ativos_investigados(frame, outputfolder=out, filename='06-relacao-ativos-investigacao.png'):
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
    plt.savefig(path.join(outputfolder, filename))

# %%

def chart07_media_movel(frame, days=7, outputfolder=out, filename='07-media-movel.png'):
    plt.figure()
    ax = frame['ATIVOS'].plot()
    ax = frame['ATIVOS'].rolling(days).mean().plot()
    _ = ax.set_title(f"SAP - Covid-19 - Média Móvel {days} dias")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid()
    sns.despine(left=True)
    plt.savefig(path.join(outputfolder, filename))


# %%

def chart08_evolucao_obitos(frame, outputfolder=out, filename='08-evolucao-obitos.png'):
    fig = sns.relplot(kind="line", data=frame['OBITOS'], height=5, aspect=2)
    ax = fig.facet_axis(0,0)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set(yticks=range(4,20))
    sns.despine(left=True)
    _ = fig.set(title="Evolução da quantidade de óbitos")
    plt.tight_layout()
    plt.savefig(path.join(outputfolder, filename))


# %%
def chart09_evolucao_obitos_mes(frame, outputfolder=out, filename='09-evolucao-obitos-por-mes.png'):
    plt.figure()
    deaths = frame['OBITOS_DIA']

    groupdeaths = deaths.groupby([(deaths.index.year),(deaths.index.month)]).sum()

    def formatter(label):
        yearDict = {
            2020 : '20',
            2021 : '21',
            2022 : '22'
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
    # labels
    labels = [formatter(label) for label in groupdeaths.index]

    ax = groupdeaths.plot(kind='bar', color='steelblue')

    ax.set(title='SAP COVID-19 - Total de mortes por mês')
    ax.xaxis.grid(False)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticklabels(labels)
    ax.set_xlabel("Meses")
    ax.tick_params(axis="x", rotation=0)
    sns.despine(left=True)
    plt.savefig(path.join(outputfolder, filename))

# %%

def chart10_novos_casos_recuperacoes_semanal(frame, outputfolder=out, filename='10-relacao-novos-casos-recuperados-semanal.png'):
    df2 = frame.resample('W-MON').sum()['2020-11':]

    figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 7), sharex=False)
    ax1.set_title("Relação entre confirmados e recuperados por semana")

    loc = plticker.MultipleLocator(base=3.0)
    labels = [date.strftime("%d/%m") for date in df2.index]

    sns.barplot(x=labels,
                y=df2['CONFIRMADOS_DIA'],
                color='steelblue',
                ax=ax1)
    ax1.xaxis.set_major_locator(loc)
    ax1.yaxis.grid(True)
    ax1.set_ylabel('Confirmados por semana')

    sns.barplot(x=labels,
                y=df2['RECUPERADOS_DIA'],
                color='orange',
                ax=ax2)
    ax2.yaxis.grid(True)
    ax2.xaxis.set_major_locator(loc)
    ax2.set_ylabel("Recuperados por semana")

    sns.despine(left=True)

    plt.savefig(path.join(outputfolder, filename))

# %%

if __name__ == "__main__":
    frame = read_data(inputfile)

    chart06_relacao_ativos_investigados(frame)
    chart10_novos_casos_recuperacoes_semanal(frame)
    chart09_evolucao_obitos_mes(frame)
    chart05_relacao_confirmados_recuperados(frame)