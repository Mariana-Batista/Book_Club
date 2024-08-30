# Books Club - ETL e Pipeline
Bem-vindo ao meu repositório de estudos e projetos em Engenharia de Dados! Este espaço foi criado para documentar minha especialização nessa área e para compartilhar os conhecimentos e projetos que venho desenvolvendo ao longo do tempo.

## Descrição do Projeto
O projeto Club Books foi desenvolvido para atender às necessidades da startup Book Club, que atua no setor de troca e venda de livros. O objetivo principal era construir uma pipeline de ETL (Extração, Transformação e Carregamento) que pudesse coletar dados de livros de uma fonte online, transformá-los para análise e carregá-los em um banco de dados MySQL. Esses dados seriam utilizados para criar um sistema de recomendação, melhorando a experiência dos usuários da plataforma.

## Estrutura e Fluxo do Projeto
### 1. Configuração do Ambiente de Desenvolvimento
<ul>
  <li>Criação do Ambiente Virtual: 
    <p>Um ambiente virtual foi criado para isolar as dependências do projeto e evitar conflitos com outros projetos. Foi utilizado o comando python -m venv .venv para criar o ambiente, e posteriormente, foi ativado utilizando source .venv/bin/activate (no Windows, .\venv\Scripts\activate).</p></li>
  <li>Instalação das Dependências: 
    <p>As dependências necessárias foram instaladas utilizando um arquivo requirements.txt. Esse arquivo lista todas as bibliotecas e suas versões que o projeto necessita, como Scrapy, Pandas, MySQL Connector, APScheduler, entre outras. </p></li>
</ul>

### 2. Extração de Dados com Scrapy
<ul>
  <li>Configuração e Desenvolvimento do Spider Scrapy:
    <p>Foi desenvolvido um Spider utilizando o framework Scrapy para extrair dados do site Books to Scrape.
    <p>O Spider foi configurado para navegar pelas páginas do site e coletar informações essenciais como o nome do livro, categoria, número de estrelas, preço e disponibilidade em estoque.
   <p>Os dados extraídos foram inicialmente armazenados em um arquivo JSON, localizado em ..\Club_Books\data\raw\books.json.</li>
</ul>

### 3. Transformação de Dados com Pandas

<ul>
  <li>Processamento e Transformação dos Dados:
    <p>Um script Python utilizando a biblioteca Pandas foi criado para transformar os dados extraídos.</p></li>
  <li>
    As transformações incluíram:
    <ul>
      <li>Criação de uma coluna 'date_extract' que armazena a data e hora da extração dos dados.</li>
      <li>Adição de uma coluna 'source', indicando a URL de origem dos dados.</li>
      <li>Conversão da coluna 'price' para o tipo 'float'.</li>
      <li>Conversão da coluna in_stock para o tipo int, substituindo valores nulos por zero.</li>
    </ul>
  </li>
  <li>Após a transformação, os dados foram salvos em ..\Club_Books\data\processed\books_transform.json.</li>
</ul>

### 4. Carregamento de Dados no MySQL

<ul>
  <li>Criação e Conexão ao Banco de Dados MySQL:
  <p>Utilizando a biblioteca mysql-connector-python, foi estabelecida uma conexão com o servidor MySQL.</p>
  <p>Um banco de dados chamado book_club_db foi criado, junto com uma tabela books para armazenar os dados transformados.</p></li>
  <li>Inserção dos Dados Transformados:
  <p>O script de carregamento leu o arquivo JSON transformado e inseriu os dados na tabela books do banco de dados MySQL.</p>
  <p>Erros e exceções foram tratados durante o processo para garantir a integridade dos dados.</p></li>
</ul>

### 5. Automatização com APScheduler
<ul>
  <li>Criação do Pipeline Diário:
    <p>Um pipeline diário foi criado utilizando a biblioteca APScheduler.
  </li>
  <li>O pipeline foi configurado para executar todos os dias às 14:30, realizando as seguintes tarefas:
  <p>Executar o Spider Scrapy para extrair novos dados.</p>
  <p>Transformar os dados extraídos.</p>
  <p>Carregar os dados transformados no banco de dados MySQL.</p>
  <p>O pipeline foi projetado para rodar em segundo plano, e foi implementado um loop infinito que mantém o agendador ativo, exceto em caso de interrupção manual.</p></li>
</ul>

### 6. Execução e Teste
<ul>
  <li>Execução Manual e Automática:
    <p>Os scripts de ETL foram testados manualmente para garantir que cada etapa (extração, transformação e carregamento) funcionasse corretamente.</p>
    <p>O pipeline automatizado foi configurado e testado para assegurar que as execuções diárias ocorreriam conforme o planejado.</p></li>
  <li>Tratamento de Erros:
  <p>Durante a execução, foram adicionados blocos de tratamento de exceções para capturar e relatar qualquer erro, garantindo que o pipeline possa ser monitorado e depurado de forma eficaz.</p></li>
</ul>

## Componentes
### 1. Spider Scrapy:
<ul>
  <li>Localização: 'src/club_books/spiders/books.py'.</li>
  <li>Função: Extrai dados de livros do site Books to Scrape.</li>
</ul>

### 2. Transformação de dados:
<ul>
  <li>Localização: 'etl/transform/transform_data.py'</li>
  <li>Função: Processa e transforma os dados extraídos, adicionando informações adicionais e ajustando o formato.</li>
</ul>

### 3. Carregamento de dados:
<ul>
  <li>Localização: 'etl/load/load_data.py'</li>
  <li>Função: Carrega os dados transformados no banco de dados MySQL.</li>
</ul>

### 4. Pipeline Diário:
<ul>
  <li>Localização: 'pipelines/daily_etl_pipeline.py'
  <li>Função: Agendador que executa os scripts de ETL diariamente às 00:00.</li>
</ul>
