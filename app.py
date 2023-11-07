from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json
import pyodbc
import os

app = Flask(__name__)
CORS(app)

# Função para conectar ao banco de dados
def connect_to_db():
    server = 'laywerestudeia.database.windows.net'
    database = 'laywer'
    username = 'estudeiaadmin'
    password = os.getenv('AZURE_DB_PASSWORD')  # Use variável de ambiente para a senha
    driver = '{ODBC Driver 17 for SQL Server}'
    conn_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(conn_str)

# Função para salvar a petição no banco de dados
def save_petition(petition_text):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Petitions (Content) VALUES (?)", petition_text)
    conn.commit()
    conn.close()

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json
    print("Dados recebidos:", data)
    script_path = 'C:/Users/Allan/OneDrive/Área de Trabalho/advogado/api2.py'

    response = subprocess.run(
        ['python', script_path, json.dumps(data)], 
        capture_output=True, 
        text=True
    )
    print("STDOUT:", response.stdout)
    print("STDERR:", response.stderr)

    # Salvar a resposta da petição no banco de dados
    save_petition(response.stdout)

    print("Resposta do subprocess:", response.stdout)
    return jsonify({"response": response.stdout})

if __name__ == '__main__':
    app.run(debug=True)
