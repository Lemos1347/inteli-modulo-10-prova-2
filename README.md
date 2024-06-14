# Inteli Módulo 10 Prova 2

O que deve ser desenvolvido:

1. Realizar a adequação do projeto desenvolvido em Flask para FastAPI (até 1.0 ponto).

2. Adicionar o log em todas as rotas do sistema. O log deve ficar armazenado em um arquivo. Logar apenas informações de nível WARNING em diante (até 3.0 pontos).

3. Implementar o sistema em um container docker (até 1.0 ponto).

4. Adicionar um container com um Gateway utilizando NGINX para o sistema (até 2.0 pontos).

5. Criar um arquivo docker-compose que permita executar toda a aplicação (até 2.0 pontos).

6. Implementar os testes da API com Insomnia (até 1.0 ponto).

# Esquema de pastas

## [backend](./backend/)

Aqui está o código do backend da aplicação. Pode ser encontrado o Dockerfile, o arquivo de log, o código em python dentro da pasta `src` e o arquivo de requirements da aplicação.

## [gateway](./gateway/)

Aqui está o código do gateway da aplicação feito com nginx. Pode ser encontrado o Dockerfile e o arquivo de configuração do NGINX.

## root

Na root desse projeto está o arquivo [docker-compose.yml](./docker-compose.yml) que é responsável por orquestrar a execução dos containers e a [collection do Insomnia](./Insomnia_collection.json) para testar a API.

# Executando a aplicação

## Docker Compose

Para executar a aplicação, basta executar o comando `docker-compose up` na pasta raiz do projeto. O docker-compose irá criar os containers e orquestrar a execução deles. O backend estará disponível em `http://localhost:3000`(o nginx foi mapeado para rodar na porta 3000 do host no docker compose) com as seguinte rotas:

- GET /blog
- POST /blog
- GET /blog/{id}
- PUT /blog/{id}
- DELETE /blog/{id}

## Local

Para executar a aplicação sem docker basta apenas entrar na pasta [backend](./backend/), instalar as blibliotecas:

```bash
pip install -r requirements.txt
```

E executar:

```bash
fastapi run src/main.py
```

O backend estará disponível em `http://localhost:8000` com as seguinte rotas:

- GET /blog
- POST /blog
- GET /blog/{id}
- PUT /blog/{id}
- DELETE /blog/{id}

# Logs

Todos os logs gerados pela aplicação estão sendo armazenados no arquivo [backend/logs.txt](./backend/logs.txt). Apenas logs de nível WARNING ou superior estão sendo armazenados.
