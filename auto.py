from pathlib import Path

from src.viz import (lineplot_relacao_confirmados_recuperados,
                     lineplot_relacao_ativos_investigados,
                     barplot_evolucao_obitos_mes,
                     barplot_novos_casos_recuperacoes_semanal,
                     lineplot_taxa_testes_positivados, read_data)


if __name__ == "__main__":

    dest = Path('.', 'imgs')
    source = Path('.', 'data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx')

    frame = read_data(source)

    lineplot_relacao_ativos_investigados(frame, outputfolder=dest)
    barplot_novos_casos_recuperacoes_semanal(frame, outputfolder=dest)
    barplot_evolucao_obitos_mes(frame, outputfolder=dest)
    lineplot_relacao_confirmados_recuperados(frame, outputfolder=dest)
    lineplot_taxa_testes_positivados(frame, outputfolder=dest)