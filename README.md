# Projeto ZapSign Integration

Este projeto é um sistema de gerenciamento de documentos que se integra com a API da ZapSign para criação e manipulação de documentos eletrônicos. O sistema é composto por um backend em Django e um frontend em Angular, permitindo a criação, edição e visualização de documentos eletrônicos de forma eficiente e segura.

## Tecnologias Utilizadas

**Backend:** Python, Django, Django REST Framework, PostgreSQL, requests  
**Frontend:** Angular, TypeScript, Angular Material

## Configuração do Ambiente

Certifique-se de ter os seguintes requisitos instalados: Python 3.x, Node.js 14.x ou superior, PostgreSQL e, opcionalmente, Docker para execução em contêineres.

### Instalação

#### Backend

1. Crie um ambiente virtual com o comando `python -m venv venv`. Ative o ambiente virtual com:
   - **Linux/macOS:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate.bat`
2. Instale as dependências do projeto usando `pip install -r requirements.txt`.
3. Configure o banco de dados no arquivo `settings.py` com suas credenciais do PostgreSQL. Um exemplo de configuração é:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nome_do_banco',
           'USER': 'usuario',
           'PASSWORD': 'senha',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
4. Execute as migrações para criar as tabelas no banco de dados com o comando `python manage.py migrate`.
5. Configure a API ZapSign no arquivo `settings.py` com suas credenciais, utilizando variáveis de ambiente para maior segurança. Um exemplo de configuração é:
   ```python
   ZAPSIGN_API_KEY = os.getenv('ZAPSIGN_API_KEY')
   ```

## Frontend

O frontend é implementado em Angular, utilizando componentes standalone para uma estrutura mais modular e escalável. Ele se comunica com o backend através de um serviço `DocumentService` que faz requisições HTTP para a API Django.

**Principais Componentes**

* `AppComponent`: Componente raiz da aplicação, responsável por exibir o formulário de criação de documentos e a lista de documentos.
* `DocumentFormComponent`: Componente standalone que contém o formulário para criar novos documentos.
* `DocumentListComponent`: Componente standalone que exibe a lista de documentos e permite a edição e exclusão.
* `DocumentService`: Serviço que encapsula a lógica de comunicação com o backend, incluindo as operações CRUD de documentos.

**Configuração**

1. Navegue até a pasta do frontend com `cd frontend`.
2. Instale as dependências do projeto usando `npm install`.
3. Configure as URLs da API no arquivo `src/environments/environment.ts`. Um exemplo de configuração é:
   ```typescript
   export const environment = {
     production: false,
     apiUrl: 'http://localhost:8000/api/v1/'
   };
   ```

### Execução do Projeto

- **Backend:** Use o comando `python manage.py runserver`. O backend estará disponível em [http://localhost:8000](http://localhost:8000).
- **Frontend:** Use o comando `ng serve` e acesse o frontend em [http://localhost:4200](http://localhost:4200).

### Testes

- **Backend:** Use o comando `python manage.py test`.
- **Frontend:** Use o comando `ng test`.

### Autenticação e Integração com a API ZapSign

O backend obtém um token JWT da ZapSign para autenticar as requisições. A criação de documentos é feita através de requisições autenticadas ao endpoint `/api/v1/docs/` da API ZapSign.

### Considerações Finais

Este projeto demonstra a integração entre Django, Angular e a API ZapSign. Lembre-se de proteger suas credenciais da ZapSign usando variáveis de ambiente e revise as configurações de segurança antes de implantar em produção. Este guia é um ponto de partida; você precisará implementar a lógica completa de integração, incluindo tratamento de erros e validação de dados.
