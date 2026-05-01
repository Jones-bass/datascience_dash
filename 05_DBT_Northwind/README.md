[project]
name = "05-dbt-northwind"
version = "0.1.0"
description = ""
authors = [
    {name = "jones-bass",email = "jonesdev.tb@gmail.com"}
]
requires-python = ">=3.13"
dependencies = [
    "dbt-postgres (>=1.10.0,<2.0.0)"
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry# Projeto dbt - Guia Inicial

Este projeto usa **dbt** para transformar dados em um banco PostgreSQL.

---

## Docker 

```bash
docker compose up -d

```

## 1. Criar ambiente 

```bash
Criar ambiente virtaul
python -m venv venv"

```bash
Iniciar o poetry e DBT
poetry init
poetry add dbt-postgres
dbt init (passar a confi do banco)

dbt debug (Testar conexão com o banco)
dbt seed (atualizar ou criar tabelas)
dbt seed --full-refresh (Rodar a seed)
dbt run (Rodas as models "views")




