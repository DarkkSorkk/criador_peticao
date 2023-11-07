import pyodbc

# Substitua os detalhes pelos seus dados reais de conexão
connection_string = (
)

# Estabelecendo a conexão
try:
    conn = pyodbc.connect(connection_string)
    print("Conexão estabelecida com sucesso.")
    # Aqui você pode adicionar operações com o banco de dados
    conn.close()
except Exception as e:
    print("Ocorreu um erro ao conectar ao banco de dados:", e)
