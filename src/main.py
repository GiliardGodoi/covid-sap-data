import os
from datetime import datetime
from pathlib import Path

import click
from rich.console import Console
from rich.traceback import install

from .manual_collector_cli import ask4date, ask4int, ask4YesOrNo, greeting

from .viz import (lineplot_relacao_confirmados_recuperados,
                     lineplot_relacao_ativos_investigados,
                     barplot_evolucao_obitos_mes,
                     barplot_novos_casos_recuperacoes_semanal,
                     lineplot_taxa_testes_positivados, read_data)

install()
console = Console()

@click.group()
def cli():
    pass


@cli.command()
@click.option('--filename',
                default=Path('.', 'data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx'),
                help='open excel file')
def excel(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    os.startfile(filename)


@cli.command()
@click.option('--many',
                is_flag=True,
                default=False,
                help='enter data by hand')
def entry(many : bool):


    fields = [
        "Data",
        "Descartados",
        "Em investigação",
        "Confirmados",
        "Examinados",
        "Recuperados",
        "Ativos",
        "Hospitalizados",
        "Domicílio",
        "Óbitos"
    ]

    columns = [
        "DATA",
        "DESCARTADOS",
        "EM INVESTIGACAO",
        "CONFIRMADOS",
        "EXAMINADOS",
        "RECUPERADOS",
        "ATIVOS",
        "HOSPITAL",
        "DOMICILIO",
        "OBITOS"
    ]

    msg = '''
    # Boletins Diário Santo Antônio da Platina - PR
    Utilitário para coletar os dados dos boletins diários sobre os casos de *COVID-19* no Município de Santo Antônio da Platina - PR
    '''

    greeting(msg)

    width = max(len(f) for f in fields) + 2

    data = list()

    go_on = True

    while go_on:
        line = list()
        for i, field in enumerate(fields):
            if i == 0:
                ans = ask4date(f"{field}:", justify='left', width=width, default=datetime.now())
            else:
                ans = ask4int(f"{field}:", justify='left', width=width, default=0)
            line.append(ans)
        go_on = ask4YesOrNo("Deseja continuar?")
        data.append(line)

    print(data)

@cli.command()
@click.option('--source',
                default=Path('.', 'data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx'),
                help='point to the file if the given data')
def draw(source):


    dest = Path('.', 'data', 'charts')

    with console.status("[bold green] Lendo arquivo..."):
        frame = read_data(source)

    with console.status("Plotando gráficos...", spinner='clock'):
        lineplot_relacao_ativos_investigados(frame, outputfolder=dest)
        barplot_novos_casos_recuperacoes_semanal(frame, outputfolder=dest)
        barplot_evolucao_obitos_mes(frame, outputfolder=dest)
        lineplot_relacao_confirmados_recuperados(frame, outputfolder=dest)
        lineplot_taxa_testes_positivados(frame, outputfolder=dest)

if __name__ == "__main__":
    cli()
