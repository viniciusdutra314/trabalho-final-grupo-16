# trabalho-final-grupo-16

### Configuração docker
Para a fácil reprodução do ambiente de desenvolvimento em diferentes maquinas e
sistemas operacionais, foi criado um `docker-compose.yaml` com dois containers conectados
em rede, uma imagem do banco de dados PostgreSQL na porta 5432 e outra com um pgadmin na porta 8080.

As credências do pgadmin podem ser encontradas nas variáveis de ambiente 
`PGADMIN_DEFAULT_EMAIL` e `PGADMIN_DEFAULT_PASSWORD`, já a conexão com 
o banco pode ser encontrada em `POSTGRES_USER` e `POSTGRES_PASSWORD`. 


### Configuração Python

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
