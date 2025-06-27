#!/bin/bash

echo "▶️ Criando ambiente virtual..."
python3 -m venv myvenv
source myvenv/bin/activate

echo "✅ Ambiente virtual ativado!"

echo "📦 Instalando dependências locais com constraints do Airflow..."
pip install --upgrade pip
pip install -r requirements.txt \
  --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.8.txt

echo "✅ Dependências instaladas!"

echo "🧼 Limpando containers e volumes antigos (se existirem)..."
docker-compose down -v --remove-orphans

echo "🛠️ Inicializando banco de dados do Airflow e criando o usuário..."
docker-compose up airflow-init

echo "🚀 Iniciando webserver e scheduler do Airflow..."
docker-compose up -d webserver scheduler

echo "🌐 Acesse o Airflow em: http://localhost:8080"
echo "🔐 Login: airflow | Senha: airflow"

echo "✅ Pronto! Execute a DAG 'brewery_etl_pipeline' pela interface."


## chmod +x setup_bees_case.sh
## ./setup_bees_case.sh
