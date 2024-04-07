# Analisando os dados da COVID-19 para uma cidade do interior do Paraná. O que podemos inferir?

Santo Antônio da Platina (SAP) é uma cidade no Norte Pioneiro do Paraná. Diariamente a Prefeitura local divulga boletins com dados sobre a situação local da COVID-19. Mas o que esses dados podem nos dizer?

E diariamente também os meios de divulgação divulgam uma profusão de gráficos, numeros e informações sobre a COVID-19.
Como ela se desenvolve nos Estados, no Brasil e talvez no Mundo.

Mas e enquanto a situação na sua cidade?

A motivação para esse projeto parte da premissa de pensarmos globalmente, mas agirmos localmente. E que isso possa fazer alguma diferença na vida em nossas comunidades.

Quer contribuir? *Fork, code and pull*. Ou entre em contato e saiba como.

## Evolução dos casos ativos e em investigação

![alt text "Não conseguiu visualizar? Vá para a pasta data\charts"](data/charts/06-relacao-ativos-investigacao.png)

## Relação entre novos casos e recuperados por semana

![alt text "Não conseguiu visualizar? Vá para a pasta data\charts"](data/charts/10-relacao-novos-casos-recuperados-semanal.png)

## Número de óbitos por mês

![alt text "Não conseguiu visualizar? Vá para a pasta  data\charts"](data/charts/09-evolucao-obitos-por-mes.png)

## Relação casos confirmados e recuperados

![alt text "Não conseguiu visualizar? Vá para a pasta  data\charts"](data/charts/05-relacao-confirmados-recuperados.png)

## Percentual de testes positivados

![alt text "Não conseguiu visualizar? Vá para a pasta data\charts"](data/charts/11-taxa-testes-positivados.png)

A última porcentagem informada no gráfico deve ser interpretada com cuidado, talvez como uma tendência, uma vez que a semana não está concluída, esse número pode sofrer alterações abruptas.

## Referências

[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html), do cientista Jake VanderPlas.

Para instalar na sua máquina siga os seguites passos:

```shell
git clone https://github.com/GiliardGodoi/covid-sap-city.git
cd covid-sap-city
pip install .
```

Outros projetos:

- [COVID19-AutoReports](https://github.com/ramongss/COVID19-AutoReports) mantindo por [@ramongss](https://github.com/ramongss), e;
- [Painel COVID-19](https://brasil.io/covid19/) mantido pela organização Brasil IO.
