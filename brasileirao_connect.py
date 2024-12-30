# Bilioteca necessária para conectar ao banco de dados SQLite
import sqlite3
import pandas as pd

# Carregar o DataFrame a partir do arquivo CSV
tabela_classificacao = pd.read_csv('tabela_classificacao.csv')

conn =  sqlite3.connect('brasileirao.db')  # Variável de conexão
# cursor = conn.cursor()  # Variável que designa onde vai ser executado o comando SQL

# Enviar os valores do dataframe para a tabela 'classificacao'
tabela_classificacao.to_sql('classificacao', conn, if_exists='replace', index=False)
print(tabela_classificacao)

# Fechar a conexão
conn.close()