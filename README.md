# Books Club - ETL e Pipeline
Bem-vindo ao meu repositório de estudos e projetos em Engenharia de Dados! Este espaço foi criado para documentar minha especialização nessa área e para compartilhar os conhecimentos e projetos que venho desenvolvendo ao longo do tempo.

## Descrição
O projeto Club Books é uma solução de engenharia de dados desenvolvida para a startup Book Club. O sistema é responsável pela extração, transformação e carregamento (ETL) de dados de livros para um banco de dados MySQL, visando auxiliar na recomendação e análise de livros para troca e venda.

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
