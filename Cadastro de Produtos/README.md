# Cadastro De Cliente Django

![GitHub repo size](https://img.shields.io/github/repo-size/Drack112/Treina-Web-Django?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Drack112/Treina-Web-Django?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Drack112/Treina-Web-Django?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/Drack112/Treina-Web-Django?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/Drack112/Treina-Web-Django?style=for-the-badge)

> Código que foi executado e reproduzido durante o curso de Django da Treina Web

### Funções e adeptos

- [x] Crud de Clientes
- [x] Interface Administrativa customizada
- [x] Suporte para banco de dados externos
- [x] Uso de cache

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->

- Você instalou a versão mais recente de `< Docker/ Python / Makefile >`
- Você tem uma máquina `< Windows / Linux / Mac >`.
- Você possui um `< editor de código / Gerenciador de banco de dados >`.

## 🚀 Instalando

```bash
$ pip install -r requirements
```

## ☕ Rodando

Preencha o arquivo `.env.example` com as informações cobradas e depois renomeie para `.env`.

```env
SECRET_KEY=
DEBUG=
HOSTS=127.0.0.1 [::1] localhost

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

# Dados opcionais
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

Crie um banco de dados com o docker-compose

```bash
$ docker-compose up db
```

Agora realize as migrações necessárias:

```bash
$ make migrations && make migrate
```

E por fim, rode o aplicativo:

```bash
$ make runserver
```
