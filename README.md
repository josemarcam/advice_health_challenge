# Advice Health Challenge

versão python 3.11.0

## Pré-requisitos

### 1.Iniciando Docker

Na raiz do projeto existe um arquivo `docker-compose.yml` para rodar, precisamos ter instalado o docker e docker-compose. Para rodar o docker-compose:
  

    docker-compose build

    docker-compose up # existe a opção -d para deixar o docker rodando em segundo plano

Estamos subindo 2 containers, o primeiro com o **Mysql** e um outro com a aplicação **Flask**

Após a inicialização dos containers e antes de usar o sistema, precisamos criar o primeiro usuário, para isso

    docker ps # pegue o id do container mysql
    docker exec -it {id_do_container} bash

    python -m flask shell

    from src.infra.orm.factories.user import UserFactory
    UserFactory(email="email@email.com")

Pronto, agora temos o usuários com email **email@email.com** e senha **123qwe**.

### 2. Acessando a aplicação

Após o primeiro passo, a aplicação estará disponível em **localhost:5001**.

Para facilitar, disponibilizei uma collection de requests com nome de **advice_health_challenge.postman_collection.json**

Para usar essa collection, apenas importe no **postman** ou no **insomnia**.