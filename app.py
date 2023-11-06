from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json
    # Caminho completo para o script api2.py
    script_path = 'C:/Users/Allan/OneDrive/Área de Trabalho/advogado/api2.py'

    # Chamar o script api2.py e passar os dados como argumento
    response = subprocess.run(
        ['python', script_path, json.dumps(data)], 
        capture_output=True, 
        text=True
    )
    return jsonify({"response": response.stdout})

if __name__ == '__main__':
    app.run(debug=True)
