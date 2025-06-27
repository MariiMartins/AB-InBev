# BEES Data Engineering Case - Cervejarias 🍻

## ✨ Visão Geral

Este projeto resolve o desafio proposto pela BEES, que consiste em consumir dados da API Open Brewery DB e armazená-los em um data lake, utilizando a arquitetura Medallion (Bronze, Silver, Gold). O pipeline é orquestrado com Apache Airflow e executado em containers Docker.

---

## 📚 Arquitetura

```text
airflow/
  ├── dags/
  │   └── brewery_pipeline.py
scripts/
  ├── extract.py       # Bronze: coleta os dados da API
  ├── transform.py     # Silver: trata e formata os dados
  └── aggregate.py    # Gold: agrega os dados por tipo e estado

requirements.txt
Dockerfile (opcional)
docker-compose.yml
README.md
```

---

## 🚀 Execução

### 1. Requisitos

* Docker e Docker Compose instalados

### 2. Subir o ambiente:

```bash
docker-compose up --build
```

### 3. Acessar o Airflow:

* UI: [http://localhost:8080](http://localhost:8080)
* Login: `airflow` / Senha: `airflow`

### 4. Executar a DAG:

* Ative a DAG `brewery_etl_pipeline` e execute manualmente ou aguarde o agendamento.

---

## 📃 Detalhamento das Camadas

### Bronze (Raw)

* Coleta os dados da API [https://api.openbrewerydb.org/breweries](https://api.openbrewerydb.org/breweries)
* Salva em `data/bronze/breweries_raw.csv`

### Silver (Curated)

* Remove registros incompletos
* Converte para Parquet
* Particiona por estado (`state`)

### Gold (Analytical)

* Agrega os dados: quantidade de cervejarias por tipo e estado
* Salva em `data/gold/brewery_summary.csv`

---

## 🎡 Monitoramento & Alertas

* Uso do Airflow para monitoramento e retries automáticos.
* Failures podem ser configuradas para notificação via email ou Slack (exemplo comentado na DAG).
* Logs acessíveis via Web UI do Airflow.

---

## 📊 Melhorias Futuras

* Persistência em cloud storage (ex: S3)
* Uso de Spark para processamento distribuído
* Validações com Great Expectations
* Testes com Pytest + cobertura

---

## ✅ Como Rodar os Scripts Localmente

```bash
# Extrair dados da API
python scripts/extract.py

# Transformar dados
python scripts/transform.py

# Agregar dados
python scripts/aggregate.py
```

---

## 🚮 Licença

Este projeto é apenas para fins educacionais, desenvolvido para o case BEES.
