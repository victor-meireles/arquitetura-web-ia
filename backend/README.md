# Alura Album - Backend API 🚀

Este é o servidor backend para o **Álbum de Figurinhas Virtual**, desenvolvido em Python utilizando o framework **FastAPI**. Ele é responsável por listar as figurinhas disponíveis e servir dinamicamente as imagens correspondentes.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **FastAPI:** Framework moderno e rápido para construção de APIs.
* **Uvicorn:** Servidor ASGI para rodar a aplicação FastAPI.
* **CORS Middleware:** Configurado para permitir requisições de qualquer origem (essencial para integração com o frontend).

---

## 📂 Estrutura de Pastas (Backend)

```text
backend/
├── .venv/            # Ambiente virtual do Python (dependências)
├── figurinhas/       # Pasta contendo as imagens das figurinhas (01-alan-turing.jpg, etc.)
└── main.py           # Código fonte principal do servidor FastAPI
```

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python 3 instalado no seu computador.

### 1. Ativar o Ambiente Virtual
Abra o terminal na pasta `backend/` e ative o ambiente virtual para carregar as dependências necessárias:

* **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

### 2. Executar o Servidor Uvicorn
Com o ambiente virtual ativo, inicie a API:
```bash
uvicorn main:app --reload
```
O servidor estará rodando em **`http://localhost:8000`**.

---

## 📡 Endpoints da API

A API conta com os seguintes endpoints configurados:

### 1. Listar Figurinhas
* **Rota:** `GET /figurinhas`
* **Descrição:** Retorna a lista contendo as figurinhas ativas (com ID, nome, categoria e URL da imagem correspondente).
* **Exemplo de Retorno (JSON):**
  ```json
  [
    {
      "id": 1,
      "nome": "Alan Turing",
      "categoria": "IA",
      "imagem_url": "/figurinhas/1/imagem"
    },
    ...
  ]
  ```

### 2. Servir Imagem da Figurinha
* **Rota:** `GET /figurinhas/{id}/imagem`
* **Descrição:** Retorna o arquivo físico de imagem da figurinha com base no ID fornecido na URL.
* **Funcionamento:** O servidor utiliza a biblioteca `glob` para buscar na pasta `figurinhas/` qualquer arquivo que inicie com o ID informado formatado com dois dígitos (ex: `01-alan-turing.jpg` para o ID `1`). Caso o arquivo não seja encontrado, retorna status `404 Not Found`.

---

## 📖 Documentação Automática
O FastAPI gera documentações interativas da API de forma automática. Com o servidor rodando, acesse:

* **Swagger UI:** `http://localhost:8000/docs`
* **ReDoc:** `http://localhost:8000/redoc`
