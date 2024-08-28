import mysql.connector
import pandas as pd
import os
from mysql.connector import Error

from dotenv import load_dotenv
load_dotenv()

def create_connection():
    """Create a connection to the MySQL database using environment variables."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        print("Conexão com o MySQL foi bem-sucedida")
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    return connection

def create_database(cursor):
    """Create the database if it does not exist."""
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS book_club_db")
        cursor.execute("USE book_club_db")
    except Error as e:
        print(f"Erro ao criar o banco de dados: {e}")

def create_table(cursor):
    """Create the books table if it does not exist."""
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        category VARCHAR(255),
        stars VARCHAR(50),
        price FLOAT,
        in_stock INT,
        date_extract DATETIME,
        source VARCHAR(255)
    )
    """
    try:
        cursor.execute(table_creation_query)
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")

def insert_data(cursor, data):
    """Insert data into the books table."""
    insert_query = """
    INSERT INTO books (name, category, stars, price, in_stock, date_extract, source)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for _, row in data.iterrows():
        try:
            cursor.execute(insert_query, (
                row['name'],
                row['category'],
                row['stars'],
                row['price'],
                row['in_stock'],
                row['date_extract'],
                row['source']
            ))
        except Error as e:
            print(f"Erro ao inserir dados: {e}")

def main():
    """Main function to create the database, table, and insert data."""
    # Conectar ao MySQL
    conn = create_connection()
    
    if conn:
        cursor = conn.cursor()
        create_database(cursor)
        create_table(cursor)
        
        # Carregar dados transformados
        try:
            data = pd.read_json(r'..\Club_Books\data\processed\books_transform.json', lines=True)
        except ValueError as e:
            print(f"Erro ao ler o arquivo JSON: {e}")
            return

        # Inserir dados na tabela
        insert_data(cursor, data)
        
        # Confirmar a inserção e fechar a conexão
        conn.commit()
        cursor.close()
        conn.close()
        print("Dados inseridos com sucesso no banco de dados 'book_club_db'.")

if __name__ == "__main__":
    main()



