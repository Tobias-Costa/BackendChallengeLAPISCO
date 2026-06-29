
# 📚 Book & Author API: Backend Challenge - LAPISCO

Este projeto é uma API RESTful de alta performance desenvolvida para o gerenciamento centralizado de livros e seus respectivos autores, com suporte a relacionamentos muitos-para-muitos (ManyToMany), paginação customizada e filtros de busca inteligente.

## 🛠️ Stacks Utilizadas

*   **Python** — Linguagem base do ecossistema.
*   **Django** — Framework web robusto focado em escalabilidade.
*   **Django Rest Framework (DRF)** — Toolkit especializado na construção de APIs REST.
*   **Docker & Docker Compose** — Conteinerização do ambiente isolado de desenvolvimento.
*   **Visual Studio Code** — Ambiente de Desenvolvimento Integrado (IDE).
*   **PostgreSQL** — Sistema de gerenciamento de banco de dados relacional.

## 🚀 Como Configurar o Ambiente de Desenvolvimento (Docker)

Siga os passos abaixo para clonar, configurar e rodar o projeto em um ambiente totalmente conteinerizado.

### 1. Clonar o Repositório
```bash
git clone https://github.com/Tobias-Costa/BackendChallengeLAPISCO.git
cd BackendChallengeLAPISCO
```

### 2. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na **raiz do projeto** e insira as configurações abaixo:

```env
DJANGO_SECRET_KEY = [SECRET-KEY]
DEBUG = 0
DJANGO_ALLOWED_HOSTS = [HOSTS(EX:localhost,127.0.0.1,0.0.0.0)]
DJANGO_LOGLEVEL=info

DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=[NOME-DO-DATABASE-AQUI]
DATABASE_USERNAME=[USERNAME-AQUI]
DATABASE_PASSWORD=[SENHA-AQUI]
DATABASE_HOST=[HOSTNAME-AQUI]
DATABASE_PORT=5432
```

### 3. Buildar e Inicializar os Containers
Com o arquivo `.env` configurado, inicialize a aplicação e o banco de dados com o Docker Compose:

```bash
docker-compose up --build
```
*O Docker cuidará automaticamente de ler o arquivo `.env`, baixar as imagens necessárias, instalar as dependências do `requirements.txt`, aplicar as migrations e expor o servidor.*

A API estará disponível no endereço local: `http://127.0.0.1:8000`.

Acesse a [documentação](http://127.0.0.1:8000/api/docs/) para mais informações.

---

## 🛣️ Endpoints da API

### Autores (`/api/author/`)

| Método | Endpoint | Descrição | Parâmetros da URL |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/authors/` | Lista autores paginados | Nenhum |
| **POST** | `/api/authors/` | Cria um novo autor | JSON (corpo da requisição) |
| **GET** | `/api/authors/<id>/` | Busca os detalhes de um autor | `id` (inteiro) |
| **PUT** | `/api/authors/<id>/` | Atualiza os dados de um autor | `id` (inteiro) + JSON |
| **DELETE**| `/api/authors/<id>/` | Deleta um autor específico | `id` (inteiro) |

### Livros (`/api/book/`)

| Método | Endpoint | Descrição | Parâmetros da URL |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/books/` | Lista livros filtrados e paginados | `title`, `author` *(Ex: `?author=Clarice&title=Hora`)* |
| **POST** | `/api/books/` | Cria um novo livro | JSON (Lista de IDs de autores no corpo) |
| **GET** | `/api/books/<id>/` | Busca os detalhes de um livro | `id` (inteiro) |
| **PUT** | `/api/books/<id>/` | Atualiza os dados de um livro | `id` (inteiro) + JSON |
| **DELETE**| `/api/books/<id>/` | Deleta um livro específico | `id` (inteiro) |

---

## 📚 Referências e Documentação Oficial
- https://docs.djangoproject.com/en/6.0/topics/db/examples/many_to_many/
- https://medium.com/@bhatnagar.aman1998/creating-restful-apis-in-django-rest-framework-using-class-based-views-78202e129773
- https://medium.com/@asharrahim6/demystifying-pagination-in-django-rest-framework-a-beginners-guide-75c2180879ff
- https://medium.com/django-unleashed/mastering-filters-in-django-rest-framework-web-services-455b54a51d5b
- https://www.youtube.com/watch?v=E3LUvsPWLwM
- https://medium.com/@anindya.lokeswara/efficient-api-development-in-django-rest-framework-drf-spectacular-and-postman-workspace-4dd6f860d14d
- https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-query-parameters
