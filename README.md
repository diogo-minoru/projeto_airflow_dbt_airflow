# Data Pipeline: PostgreSQL, Python, dbt e Airflow

Este projeto implementa um pipeline de dados completo para ingestão, tratamento e orquestração de dados. Utilizando as melhores práticas de engenharia de dados, como containerização, ingestão programática com Python, modelagem em camadas com o **esquema Medallion (bronze → silver → gold)** via `dbt`, e automação com **Apache Airflow**.

## Estrutura do Projeto
O projeto foi estruturado em três etapas:

1. **Banco de Dados PostgreSQL** com Docker Compose  e **Ingestão de dados via SQLAlchemy** com Python. [Repositório Etapa 1](https://github.com/diogo-minoru/projeto_airflow_dbt_local_setup)
2. **Modelagem dos dados com dbt** e o esquema Medallion. [Repositório Etapa 2](https://github.com/diogo-minoru/projeto_airflow_dbt_data_warehouse)
3. **Orquestração completa com Apache Airflow.** [Repositório Etapa 3](https://github.com/diogo-minoru/projeto_airflow_dbt_airflow)
4. Análise dos dados com Power BI. [Dashboard] ()

## Etapa 3 - Orquestração com Apache Airflow
A DAG no Airflow realiza a orquestração automática do pipeline:

# Integração entre dbt, Cosmos e Airflow

Este projeto demonstra como integrar **dbt (Data Build Tool)** com o **Apache Airflow** utilizando a biblioteca **[Cosmos](https://cosmos.astronomer.io/)**, permitindo a orquestração automatizada de modelos dbt como tarefas individuais do Airflow.

### **dbt (Data Build Tool)**
- Ferramenta de transformação de dados baseada em SQL.
- Permite criar modelos SQL versionados, reutilizáveis e testáveis.
- Executa tarefas como `dbt run`, `dbt test`, `dbt seed` para transformar dados dentro do data warehouse.

### **Apache Airflow**
- Plataforma de orquestração de workflows para automação de pipelines de dados.
- Permite agendar, monitorar e gerenciar tarefas com visualização de dependências.

### **Cosmos**
- Biblioteca desenvolvida pela [Astronomer](https://www.astronomer.io/) para integrar dbt e Airflow.
- Transforma modelos dbt em tasks do Airflow, facilitando a execução e monitoramento.
- Elimina a necessidade de criar operadores bash para rodar dbt manualmente.


## Estrutura do projeto
```bash
3_airflow/
├── dags/
│   └── dbt.log
├── dbt/
│   └── projeto_airflow_dbt_data_warehouse/
│       └── projeto_airflow_dbt/
│           └── models/
│               └── bronze.py
│               └── silver.py
│               └── gold.py
├── docker-compose.override.yml
├── Dockerfile
└── requirements.txt
```

**O diretório `projeto_airflow_dbt` é um submódulo do [repositório](https://github.com/diogo-minoru/projeto_airflow_dbt_data_warehouse).**

## O que é um submódulo?
Ao desenvolver um projeto, muitas vezes é necessário usar outro projeto, como uma biblioteca externa. Incluir o código diretamente pode dificultar personalizações e a implantação, enquanto copiar o código torna complicado manter as atualizações do projeto original.
O Git resolve esse problema com submódulos, que permitem incluir um repositório Git dentro de outro como subdiretório, mantendo os históricos de commits separados e facilitando a integração.

Exemplo de uso:
Você tem um projeto principal e quer incluir uma biblioteca customizada que está em outro repositório Git.
Com submódulos, você não precisa copiar os arquivos manualmente, apenas adiciona o repositório externo como submódulo.

Para adicionar o submódulo:
```bash
git submodule add <url>
```

Atualiza o repositório principal e sincroniza os submódulos com o commit referenciado pelo repositório principal:
```bash
git pull --recurse-submodules
```

Atualiza os arquivos do submódulo para esse commit mais recente.
```bash
git submodule update --remote
```

## Executar o Airflow
Dentro do diretório `3_airflow` executar o comando:
```bash
astro dev start
```