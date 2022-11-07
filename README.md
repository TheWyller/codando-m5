<p align="center">
<img src="https://img.shields.io/badge/python-3.10-blue">
<img src="https://img.shields.io/badge/django-4.0.5-red">
<img src="https://img.shields.io/badge/-djangorestframework-red">
<!-- <img src="https://img.shields.io/badge/Tech-Node.js-lightgrey"> -->
</p>

# API Codando

A ideia do projeto é desenvolver uma api que consiga listar as frameworks e funcionalidades de cada linguagem baseada na popularidade entre os usuários da aplicação.

Na API os usuários poderão buscar por ferramentas de linguagens novas para seus projetos, poderão inteagir com os posts de ferramentas que já utilizaram e compartilhar suas
experiencias com as ferramentas e compartilhar seus projetos que implementaram com a mesma.

## Features:

- Cadastro de usuário

- Autenticação

- Criação de posts

- Interação com posts

- Criação de comentarios

---

## Documentação:

[Documentação do projeto e endpoints](https://codandom5.herokuapp.com/api/docs/)

## Endpoint da aplicação:

[https://codandom5.herokuapp.com](https://codandom5.herokuapp.com/)

## Diagrama de Entidade Relacional

<img src="./DER-dark.jpg#gh-dark-mode-only">
<img src="./DER.jpg#gh-light-mode-only">

## Instalação do Projeto

Projeto desenvolvido no Python 3.10.

### 1. Criação do ambiente virtual

Efetue a criação do ambente virtual através do comando `python -m venv venv`, e em seguida acesse o ambiente através do comando:

#### Powershell

`.\venv\Scripts\Activate.ps1`

#### Bash

`source venv/bin/activate`

### 2. Instalação das dependencias

Efetue as instalações das dependencias utilizando o comando `pip install -r requirements.txt`.

### 3. Configuração do .env

Crie o arquivo `.env` com base no arquivo `.env.example`.

### 4. Criação da base de dados

O projeto foi desenvolvido utilizando o Postgress como base de dados, caso utilize outro banco faça as alterações correspondentes no arquivo `settings.py`.

- 4.1 Personalização das linguagens padrões <br/>
  Caso necessária a alteração das linguagens padrão, você pode alterar a lista de linguagens presente no arquivo `./language/management/generate_languages.py`

### 5. Execução das migrações

Execute as migrações utilizando o comando `./manage.py migrate` e execute o comando `python manage.py generate_languages` para popular a tabela de linguagens do banco.

### 6. Execução do server

Execute o server utilizando o comando `./manage.py runserver`
