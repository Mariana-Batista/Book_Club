import pandas as pd
from datetime import datetime

# Carregar os dados do arquivo JSON
data = pd.read_json(r'..\Club_Books\data\raw\books.json')

# Criar a coluna 'date_extract' com a data e hora da extração formatada para o MySQL
data['date_extract'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Criar a coluna 'source' com a URL de onde os dados foram extraídos
data['source'] = 'http://books.toscrape.com/'

# Converter a coluna 'price' para o tipo float
data['price'] = data['price'].replace('£', '', regex=True).astype(float)

# Converter a coluna 'in_stock' para o tipo int, substituindo valores nulos por zero
data['in_stock'] = data['in_stock'].str.extract(r'(\d+)').fillna(0).astype(int)

# Salvar os dados transformados no arquivo JSON
data.to_json(r'..\Club_Books\data\processed\books_transform.json', orient='records', lines=True)

print(r"Transformação concluída e dados salvos em '..\Club_Books\data\processed'.")
