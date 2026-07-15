# Importa a classe FastAPI do framework fastapi
from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define uma rota para o método HTTP GET no caminho raiz ("/")
@app.get("/")
def hello_world():
    # Retorna um dicionário que o FastAPI converte automaticamente em JSON
    return {"mensagem": "Olá, mundo! 🌍"}

# Define uma rota para o método HTTP GET no caminho "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna uma lista de figurinhas de exemplo (com id, nome e categoria)
    return [
        {"id": 1, "nome": "Alan Turing", "categoria": "IA"},
        {"id": 2, "nome": "John McCarthy", "categoria": "IA"}
    ]

