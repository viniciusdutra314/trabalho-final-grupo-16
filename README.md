# trabalho-final-grupo-16

Trabalho final da disciplina de Bases de Dados - 2025.1 - ICMC - USP - Prof. Mirela

Grupo: 16

Alunos:
- Breno Henrique Pelegrin da Silva (13687303)
- Carolina Souza Gomes (13687690)
- Vinícius Sousa Dutra (13686257) 

O vídeo executando as queries SQL pode ser visto no [YouTube](https://www.youtube.com/watch?v=IOVs0vP9SY0).

Licença: GNU GPL v3

## Configuração do Docker Compose
Para a fácil reprodução do ambiente de desenvolvimento em diferentes maquinas e
sistemas operacionais, foi criado um `docker-compose.yaml` com dois containers conectados
em rede, uma imagem do banco de dados PostgreSQL na porta 5432 e outra com um pgadmin na porta 8080.

As credências do pgadmin podem ser encontradas nas variáveis de ambiente 
`PGADMIN_DEFAULT_EMAIL` e `PGADMIN_DEFAULT_PASSWORD`, já a conexão com 
o banco pode ser encontrada em `POSTGRES_USER` e `POSTGRES_PASSWORD`. 

## Configuração do ambiente Python

Todas as dependências nas suas versões exatas estão no arquivo `requirements.txt`,
a versão do python usada foi o Python 3.11, para instalar a dependências basta digitar dois comandos:

A criação e ativação de um ambiente virtual

```bash
    python3 -m venv .venv && source .venv/bin/activate
```

E a instalação das dependências

```bash
    pip install -r requirements.txt
```

Os importantes relativos foram todos pensados que o interpretador do Python fosse executado na raiz do projeto, portanto, não execute os scripts dentro de nenhuma pasta

## Estrutura de diretórios e organização

O projeto está organizado da seguinte forma:

- ``scripts-sql``: onde são armazenados os scripts SQL que deveriam ser entregues, separados para cada exercicio, desde a criação das tabelas e população, até a execução de queries, criação de indices e views.
- ``diagrams``: onde são armazenados os diagramas (DE-RX e Mapeamento para o Modelo Relacional).
- ``documents``: onde são armazenados documentos extras, que estão anexados junto ao relatório enviado no Moodle.
- ``populate-db``: onde são armazenados os códigos Python relacionados a criação de dados sintéticos.
- ``schemes``: onde são armazenados os codigos Python relacionados a modelagem relacional do problema utilizando SQL Alchemy, separados de acordo com os núcleos do DE-RX.

