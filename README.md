# Projeto Final de Python

Este é um projeto desenvolvido como parte do curso de Python da Coderhouse.

**Membros do projeto:**
- Rodrigo Pereira
- Rudnei Galdino Santiago

**Índice**

1. [Integração com a API da The Movie Database](#integração-com-a-api-da-the-movie-database)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Tabelas no Banco de Dados](#tabelas-no-banco-de-dados) 


## Integração com a API da The Movie Database

Este projeto utiliza a API da [The Movie Database (TMDb)](https://developer.themoviedb.org/docs/getting-started) para realizar consultas sobre filmes e séries. Através dessa integração, é possível obter informações detalhadas sobre diversos filmes e séries, como título, avaliação, popularidade, entre outros.

### Configuração

#### 1. Cadastro na API

Para utilizar a API da TMDb, é necessário se cadastrar na plataforma e obter uma chave de acesso (API Key). O processo de cadastro pode ser feito diretamente no site oficial da API.

#### 2. Configuração do Arquivo `.env`

Após obter a chave da API, crie um arquivo chamado `.env` na pasta raiz do projeto e insira a chave obtida da seguinte forma:

```plaintext
API_KEY=chave_fornecida_pela_api_tmdb
```

#### 3. Execução do Código

O código principal do projeto está localizado no arquivo `main.ipynb`. Para realizar as consultas na API e visualizar os resultados, basta executar esse arquivo no seu ambiente de desenvolvimento.

## Estrutura do Projeto

O código do projeto está organizado em diferentes módulos, cada um com uma responsabilidade específica:

### 1. **Main**

O arquivo `main.ipynb` é o arquivo principal, onde são realizadas as consultas à API e o tratamento dos dados retornados.

### 2. **Utils**

O módulo `utils.py` contém funções responsáveis pelo tratamento dos dados obtidos da API e pela manipulação dos resultados.

#### **Função:** `get_dataframe_from_list(json_list)`

Este método recebe uma lista de dicionários, `json_list`, e extrai informações específicas para criar um `DataFrame` do `pandas`. Ele organiza as chaves `'adult'`, `'original_title'`, `'title'`, `'original_language'`, `'overview'`, `'popularity'`, `'release_date'`, `'vote_average'` e `'vote_count'` em colunas nomeadas dentro do `DataFrame`.

Parâmetros:
- `json_list` (list of dict): Uma lista de dicionários, onde cada dicionário contém informações sobre um item (por exemplo: filmes ou séries).

Retorno:
- `DataFrame`: Um `DataFrame` do `pandas` contendo as colunas extraídas da lista.


### 3. **api_connection**

Este módulo contém métodos e uma classe que fornecem funcionalidades para fazer requisições HTTP à API do TMDb, exibir notificações em caso de erro e manipular a chave de API.

#### **Função:** `get_request(url, headers=None)`

Faz uma requisição HTTP GET para a URL fornecida. Se o código de status da resposta for 200 (OK), retorna a resposta. Caso contrário, dispara uma notificação de erro.

Parâmetros:
- `url` (str): A URL para a qual a requisição GET será feita.
- `headers` (dict, opcional): Cabeçalhos adicionais para a requisição (padrão: `None`).

Retorno:
- Se a requisição for bem-sucedida (código de status 200), retorna o objeto `response` da requisição.
- Caso contrário, exibe uma notificação de erro com o código de status e a mensagem.

#### **Função:** `request_error_notification(status_code, status_message)`

Exibe uma notificação de erro caso a requisição HTTP falhe, mostrando o código de status e a mensagem de erro.

Parâmetros:
- `status_code` (int): O código de status HTTP da requisição.
- `status_message` (str): A mensagem de erro associada ao código de status.

Retorno:
- Nenhum. Apenas exibe uma notificação com o erro.

#### Classe: `Tmdb_api_key`

Classe responsável por acessar a chave da API armazenada nas variáveis de ambiente e gerar os cabeçalhos necessários para autenticação nas requisições.

##### Métodos:

- **`__init__(self)`**
  Inicializa a classe e obtém a chave da API a partir da variável de ambiente `API_KEY`.

- **`get_key(self)`**
  Retorna a chave da API.

Retorno:
- `self.key` (str): A chave da API armazenada.

- **`get_headers(self)`**
  Retorna os cabeçalhos necessários para autenticar requisições à API, incluindo o token de autenticação.

Retorno:
- `headers` (dict): Um dicionário contendo os cabeçalhos de autenticação e aceitação.

### 4. **db_connection**

Este módulo contém métodos responsáveis pela manipulação de um banco de dados SQLite utilizando `pandas` para trabalhar com tabelas, tanto para inserção quanto para consulta.

#### **Função:** `open_connection(db_name)`

Abre uma conexão com um banco de dados SQLite especificado pelo nome `db_name`.

Parâmetros:
- `db_name` (str): O nome do banco de dados SQLite.

Retorno:
- `conn` (sqlite3.Connection): Um objeto de conexão com o banco de dados.

#### **Função:** `close_connection(conn)`

Fecha a conexão com o banco de dados aberta anteriormente.

Parâmetros:
- `conn` (sqlite3.Connection): O objeto de conexão que deve ser fechado.

Retorno:
- Nenhum. Apenas fecha a conexão.

#### **Função:** `df_to_sql(dataframe, table_name, conn)`

Converte um `DataFrame` do `pandas` para uma tabela em um banco de dados SQLite, substituindo a tabela existente (se houver).

Parâmetros:
- `dataframe` (pandas.DataFrame): O `DataFrame` que será inserido na tabela.
- `table_name` (str): O nome da tabela no banco de dados onde os dados serão armazenados.
- `conn` (sqlite3.Connection): A conexão com o banco de dados SQLite.

Retorno:
- Nenhum. A tabela no banco de dados é atualizada.

#### **Função:** `get_all_tables(conn)`

Retorna uma lista de todas as tabelas presentes no banco de dados SQLite.

Parâmetros:
- `conn` (sqlite3.Connection): A conexão com o banco de dados SQLite.

Retorno:
- `df` (pandas.DataFrame): Um `DataFrame` contendo os nomes de todas as tabelas no banco de dados.

#### **Função:** `get_all_from_table(table_name, conn)`

Recupera todos os registros de uma tabela específica em um banco de dados SQLite.

Parâmetros:
- `table_name` (str): O nome da tabela da qual os dados serão extraídos.
- `conn` (sqlite3.Connection): A conexão com o banco de dados SQLite.

Retorno:
- `df` (pandas.DataFrame): Um `DataFrame` contendo todos os dados da tabela especificada.


## Tabelas no Banco de Dados

O projeto utiliza as seguintes tabelas para armazenar os dados obtidos da API:

### 1. **topratedmovies**

Tabela que contém os filmes mais bem avaliados na API.

Campos:
- `'adult'`: Se o filme é classificado como para adulto (0 = não, 1 = sim).
- `'original_title'`: Título original do filme.
- `'english_title'`: Título do filme em inglês.
- `'original_language'`: Língua original do filme.
- `'overview'`: Resumo do filme.
- `'popularity'`: Quantidade de acessos do filme na API.
- `'release_date'`: Data de lançamento.
- `'vote_average'`: Média de votos.
- `'vote_count'`: Quantidade de votos.

### 2. **topratedseries**

Tabela que contém as séries mais bem avaliadas na API.

Campos:
- `'adult'`: Se a série é classificada como para adulto (0 = não, 1 = sim).
- `'original_title'`: Título da série na língua original.
- `'english_title'`: Título da série em inglês.
- `'original_language'`: Língua original da série.
- `'overview'`: Resumo da série.
- `'popularity'`: Quantidade de acessos da série na API.
- `'release_date'`: Data de lançamento.
- `'vote_average'`: Média de votos.
- `'vote_count'`: Quantidade de votos.

### 3. **genres**

Tabela que contém os tipos de gêneros dos filmes.

Campos:
- `'id'`: Código de identificação do gênero.
- `'name'`: Nome do gênero.
