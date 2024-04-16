**(Projeto em andamento)**

# dr_doom - Backend para Gerenciamento de Conteúdo com Django REST Framework

<img src="dr_doom.webp" alt="dr_doom" width="350" height="500">

O `dr_doom` é uma aplicação em Django REST Framework desenvolvida para servir como backend para um Content Management Application (CMA), destinado ao gerenciamento de conteúdo. Este backend fornece serviços para armazenar, recuperar e gerenciar dados em forma de posts, bem como inclui funcionalidades administrativas e controle de autenticação.

## Configuração do Ambiente

Antes de iniciar, certifique-se de ter o Python e o Django instalados em sua máquina. Recomenda-se a criação e ativação de um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos para instalar as dependências necessárias:


    python -m venv venv
    source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
    pip install -r requirements.txt

Configuração do Banco de Dados
O dr_doom utiliza um banco de dados SQLite por padrão. Para configurar o banco de dados, execute os seguintes comandos:

    make migrate
### Iniciar o Servidor
### Inicie o servidor de desenvolvimento com o seguinte comando:


    make run
### O servidor estará disponível em http://localhost:8000/.

## Endpoints API
### Posts
### Listar todos os Posts:

#### Método: GET
URL: /api/posts/
Detalhes de um Post:

### Método: GET BY ID
URL: /api/posts/<post_id>/
Criar um novo Post:

### Método: POST
URL: /api/posts/
Parâmetros:
title: Título do post
content: Conteúdo do post
Atualizar um Post:

### Método: PUT
URL: /api/posts/<post_id>/
Parâmetros:
title: Novo título do post
content: Novo conteúdo do post
Excluir um Post:

### Método: DELETE
URL: /api/posts/<post_id>/
Administração
O Django Admin está disponível para gerenciar os dados. Acesse http://localhost:8000/admin/ e faça login com as credenciais de administrador.

## Autenticação
O dr_doom utiliza autenticação básica. Para acessar os endpoints autenticados, inclua o token de autenticação no cabeçalho da solicitação:

    curl -H "Authorization: Token <seu_token>" http://localhost:8000/api/posts/
#### Certifique-se de criar usuários e gerar tokens de autenticação usando o Django Admin.

### Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.


**Nota: O nome dr_doom é uma homenagem ao vilão Doutor Destino da Marvel Comics e não possui nenhuma relação oficial com a Marvel Entertainment.**