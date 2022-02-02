from pathlib import Path

from src.charts import (chart05_relacao_confirmados_recuperados,
                     chart06_relacao_ativos_investigados,
                     chart09_evolucao_obitos_mes,
                     chart10_novos_casos_recuperacoes_semanal,
                     chart11_taxa_testes_positivados, read_data)


if __name__ == "__main__":

    dest = Path('.', 'data', 'charts')
    source = Path('.', 'data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx')

    frame = read_data(source)

    chart06_relacao_ativos_investigados(frame, outputfolder=dest)
    chart10_novos_casos_recuperacoes_semanal(frame, outputfolder=dest)
    chart09_evolucao_obitos_mes(frame, outputfolder=dest)
    chart05_relacao_confirmados_recuperados(frame, outputfolder=dest)
    chart11_taxa_testes_positivados(frame, outputfolder=dest)