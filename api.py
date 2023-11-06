import openai

# Defina sua chave da API
openai.api_key = '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'

# Mensagem de sistema para estabelecer o comportamento do modelo
system_message = {
    "role": "system",
    "content": "You are a helpful virtual assistant named Ada."
}

# Exemplo de mensagem do usuário
user_message = {
    "role": "user",
    "content": "whats your name?"
}

# Combine as mensagens em uma lista
messages = [system_message, user_message]

# Prepare os dados para a requisição
data = {
    "model": "gpt-3.5-turbo",
    "messages": messages,
    "temperature": 0.7
}

# Faça a requisição para a API
response = openai.ChatCompletion.create(**data)

# Extraindo a resposta do modelo
message = response['choices'][0]['message']['content']
print(message)
