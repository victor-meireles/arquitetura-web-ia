import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define o caminho absoluto da pasta do arquivo atual
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# Define o caminho completo para a pasta que contém as imagens das figurinhas
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura o FastAPI para servir arquivos estáticos a partir da pasta de imagens na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista contendo os dados das figurinhas, incluindo o URL da imagem correspondente
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/imgs/01-alan-turing.jpg"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/imgs/02-john-mccarthy.jpg"}
]

# Endpoint GET para listar todas as figurinhas disponíveis
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista contendo as figurinhas cadastradas
    return figurinhas

