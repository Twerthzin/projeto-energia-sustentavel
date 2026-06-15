# Sistema de Monitoramento de Energia Solar

## Integrantes

| Nome | RM |
|------|-----|
| Enzo Ricardo Silva | 571333 |
| Eric Hernandes Penhalbel | 570237 |
| Joao Guilherme Figuereido | 572697 |
| Ryan Luther Roque | 572993 |
| Murilo Henrique Souza Ignacio | 573621 |
| Matheus Borges Soares | 574085 |

## Descricao do Projeto

Este projeto consiste em um prototipo funcional simulado de um sistema de monitoramento de energia solar fotovoltaica para residencias. O sistema demonstra a viabilidade tecnica de uma solucao que permite acompanhar a geracao de energia, o consumo residencial, o balanco energetico e os impactos ambientais e economicos.

## Objetivos

- Demonstrar uma funcionalidade operacional do sistema proposto
- Justificar tecnicamente os componentes e a arquitetura utilizados com base em eficiencia energetica e sustentabilidade
- Apresentar dados gerados pelo sistema, reais ou simulados
- Comprovar a viabilidade tecnica inicial como prova de conceito

## Arquitetura do Sistema

O sistema e composto por 5 componentes principais:

1. **Simulador de Geracao Solar**: Gera dados horarios de producao de energia baseados na irradiancia solar tipica da regiao Sudeste
2. **Simulador de Consumo Residencial**: Gera dados de consumo horario baseados em perfil residencial tipico
3. **Calculadora de Balanco Energetico**: Compara geracao e consumo para identificar excedentes ou deficits
4. **Calculadora de Sustentabilidade**: Estima CO2 evitado e equivalente em arvores
5. **Visualizador Grafico**: Apresenta os dados em formato grafico para facilitar a analise

## Diagrama do Sistema

[Dados de Irradiancia] -> [Simulador de Geracao] -> [Calculo de Balanco] -> [Metricas de Sustentabilidade]
[Dados de Consumo]      -> [Simulador de Consumo] -> [Calculo Economico]  -> [Visualizacao Grafica]

## Justificativas Tecnicas

### Eficiencia Energetica

- O sistema utiliza um painel fotovoltaico simulado de 5kWp, dimensionado para uma residencia media
- O fator de capacidade calculado (media de 15-18%) esta alinhado com sistemas reais no Brasil
- O monitoramento horario permite identificar momentos de excedente para otimizacao do consumo

### Sustentabilidade

- A geracao solar fotovoltaica emite zero CO2 durante operacao
- O sistema calcula a reducao da pegada de carbono comparada a energia da rede
- Sao apresentados equivalentes em arvores plantadas para facilitar a compreensao do impacto ambiental

### Componentes

- **Dados simulados**: Baseados em irradiancia solar real da regiao Sudeste (fonte: INMET)
- **Eficiencia do sistema**: Considera perdas por inversor, temperatura e sombreamento
- **Tarifa de energia**: Baseada na media nacional (R$ 0,90/kWh)

## Instrucoes de Uso

### Pre-requisitos

- Python 3.7 ou superior
- Bibliotecas: pandas, matplotlib, numpy

### Instalacao

pip install pandas matplotlib numpy

### Execucao

python monitoramento_solar.py

### Saida do Sistema

- Relatorio completo no console com:
  - Balanco energetico diario
  - Metricas de eficiencia
  - Impacto ambiental
  - Viabilidade economica
  - Analise horaria detalhada
- Grafico gerado: monitoramento_solar_prova_conceito.png

## Resultados Obtidos

### Balanco Energetico Diario

- Energia gerada: aproximadamente 45 kWh/dia
- Energia consumida: aproximadamente 21 kWh/dia
- Excedente: aproximadamente 24 kWh/dia

### Impacto Ambiental

- CO2 evitado: cerca de 3,8 kg/dia
- Equivalente anual: 1.387 kg de CO2/ano
- Arvores equivalentes anuais: aproximadamente 77 arvores

### Viabilidade Economica

- Economia anual estimada: R$ 14.800,00
- Payback estimado do sistema: 4 a 5 anos

## Conexao com Energias Renovaveis e Sustentabilidade

O sistema esta diretamente alinhado aos conceitos de energias renovaveis trabalhados no semestre:

1. **Fonte renovavel**: Energia solar e inesgotavel e limpa
2. **Reducao de emissoes**: Cada kWh gerado evita emissao de CO2 da rede eletrica
3. **Eficiencia energetica**: Monitoramento permite otimizar o consumo nos horarios de maior geracao
4. **Escalabilidade**: A solucao pode ser aplicada em residencias, comercios e industrias

## Prova de Conceito

A viabilidade tecnica do prototipo e comprovada por:

1. O sistema executa e gera dados consistentes
2. Os calculos seguem fundamentos tecnicos reais (irradiancia, eficiencia de paineis, fator de capacidade)
3. As metricas de sustentabilidade utilizam fatores de emissao oficiais (ONS)
4. O codigo pode ser adaptado para hardware real com sensores e inversores

## Link do Video de Demonstracao

[INSERIR LINK DO YOUTUBE AQUI]

## Tecnologias Utilizadas

- Python 3
- Matplotlib (visualizacao)
- Numpy (calculos numericos)
- GitHub (versionamento)

## Conclusao

O prototipo demonstra que um sistema de monitoramento de energia solar e tecnicamente viavel, economicamente atrativo e ambientalmente benefico. A solucao pode ser implementada com hardware real, utilizando sensores de irradiancia, medidores de consumo e um inversor fotovoltaico, mantendo a mesma logica apresentada na simulacao.
