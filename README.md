# Alura Album - Copa do Mundo Tech ⚽💻

Este projeto é um **álbum de figurinhas virtual, interativo e imersivo** feito para homenagear personalidades e grandes mentes da tecnologia no Brasil e no mundo. O álbum está dividido em categorias como Inteligência Artificial, Linguagens de Programação, Bancos de Dados, Sistemas Operacionais e Educadores Brasileiros.

O projeto conta com uma arquitetura moderna dividida entre um **Frontend estático** com visual premium e um **Backend dinâmico em Python (FastAPI)**.

---

## 📂 Estrutura do Projeto

O repositório é organizado de forma modular em duas pastas principais:

* **`/frontend`**: Interface do usuário construída com HTML5, CSS3 (Vanilla) e JavaScript puro. Apresenta efeitos sonoros com a *Web Audio API* e a simulação 3D de livro físico utilizando a biblioteca *St.PageFlip*.
* **`/backend`**: API construída em Python com *FastAPI* que gerencia a lista de figurinhas e disponibiliza as imagens como recursos estáticos dinamicamente.

---

## 🛠️ Tecnologias e Funcionalidades

### Frontend
* **Visual Cyberpunk/Tech:** Estilizado em modo escuro com cores neon e fontes modernas da Google Fonts (`Inter` e `Outfit`).
* **Enquadramento Perfeito:** Estilização responsiva sem frestas nas molduras e centralização ideal para as imagens das figurinhas.
* **Efeito Sonoro Dinâmico:** Geração sintética do som de páginas folheadas diretamente via *Web Audio API* (sem necessidade de carregar arquivos pesados de áudio).
* **Efeito Flip 3D:** Transição de páginas tridimensional e realista com *St.PageFlip*.

### Backend (API)
* **FastAPI:** Desenvolvimento ágil de endpoints assíncronos de alta performance.
* **CORS Habilitado:** Middleware configurado para permitir que o frontend faça requisições cross-origin com segurança.
* **Busca Dinâmica de Imagens:** Utilização de `glob` para encontrar e servir imagens de forma genérica a partir do ID da figurinha, independente da extensão do arquivo (`.jpg`, `.jpeg`, `.png`, `.webp`, `.avif`).

---

## 🚀 Como Executar a Aplicação Completa

Siga os passos abaixo para colocar o projeto completo para rodar localmente.

### Passo 1: Executar o Backend (API)
1. Navegue até a pasta `backend`:
   ```bash
   cd backend
   ```
2. Ative o ambiente virtual:
   * **Linux/macOS:** `source .venv/bin/activate`
   * **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   * **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
3. Execute o servidor Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   *A API estará ativa em `http://localhost:8000`.*

### Passo 2: Executar o Frontend
1. Abra um novo terminal na pasta raiz do projeto.
2. Navegue até a pasta `frontend`:
   ```bash
   cd frontend
   ```
3. Suba um servidor web simples com Python:
   ```bash
   python3 -m http.server 3000
   ```
4. Acesse **`http://localhost:3000`** no seu navegador.

*(Alternativamente, se você usa o VS Code, pode abrir a pasta `frontend` e iniciar o arquivo `index.html` usando a extensão **Live Server**).*

---

## 📡 Integração de Comunicação (API <-> Frontend)

* O Frontend se conecta à API fazendo uma chamada HTTP `fetch` para o endpoint `http://localhost:8000/figurinhas` ao inicializar a página.
* As imagens das figurinhas são requisitadas individualmente no endpoint `http://localhost:8000/figurinhas/{id}/imagem` e renderizadas nos respectivos slots do álbum.
