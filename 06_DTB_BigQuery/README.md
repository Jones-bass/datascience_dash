# dbt-core & bigqueyr

Objetivos:

1) Configurar bigquery
2) Boas práticas com sqlfluff e pre-commit
3) Ingerindo dados raw com freshness
4) Staging com yml único
5) Revisitando staging para aplicar macros
- Criando o nosso de conversão de moeda
1) Revisitando raw para aplicar macro de schema
- Criando o nosso de multiplos schemas
1) Criando nossa tabela calendário
2) Union de tabelas
3) Snapshot e SDC2

## Configuração do Projeto

### 1. Clonar o Repositório

Primeiro, Python Venv:

```bash
gpython -m venv venv
```

### 2. Inicializar o Poetry

Em seguida, inicialize o Poetry e instale as dependências:

```bash
poetry init
pip install poetry
```

### 3. Instalar Dependências Adicionais

Adicione o dbt Core, dbt-bigquery, pre-commit e sqlfluff ao ambiente do Poetry:

```bash
poetry add dbt-core dbt-bigquery
poetry add --dev pre-commit sqlfluff
```
### Configurando o Projeto com Pre-commit e SQLFluff

Neste projeto, vamos usar **pre-commit** para garantir que nosso código SQL e configuração estejam em conformidade com as melhores práticas antes de cada commit. Também usaremos **SQLFluff** para aplicar regras de formatação específicas ao nosso código SQL.

### Passos para Configuração

1. **Instalar Pre-commit e SQLFluff**
2. **Configurar Pre-commit**
3. **Configurar SQLFluff**

### 1. Instalar Pre-commit e SQLFluff

Primeiro, instale as ferramentas necessárias usando `poetry`:

```bash
poetry add --group dev pre-commit sqlfluff
```

### 2. Configurar Pre-commit

Crie um arquivo `.pre-commit-config.yaml` no diretório raiz do seu projeto com o seguinte conteúdo:

