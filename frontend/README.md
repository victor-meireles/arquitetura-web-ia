# Alura Album - Copa do Mundo Tech

Este projeto é um **álbum de figurinhas virtual e interativo** que presta homenagem a grandes nomes da tecnologia mundial e personalidades do cenário de tecnologia no Brasil. O álbum está dividido em categorias como pioneiros da Inteligência Artificial, criadores de linguagens de programação, arquitetos de bancos de dados, desenvolvedores de sistemas operacionais e educadores de tecnologia brasileiros.

O projeto foi estruturado com foco em uma experiência do usuário imersiva, utilizando efeitos visuais futuristas e interações físicas realistas.

---

## 🚀 Tecnologias Utilizadas

* **HTML5:** Estrutura semântica das páginas do álbum, botões de ação e slots de figurinhas.
* **CSS3 (Vanilla):** Estilização avançada com variáveis CSS, efeito *glitch* de texto na capa, sombras 3D realistas simulando a lombada de um livro físico e animações de colagem.
* **JavaScript (ES6+):** Lógica de controle e dinamismo da aplicação.
* **Biblioteca St.PageFlip:** Usada para criar a animação física e o efeito tridimensional de virar as páginas do álbum.
* **Web Audio API:** Utilizada para sintetizar matematicamente, no próprio navegador, o efeito sonoro de papel sendo folheado quando o usuário vira uma página.

---

## 📂 Estrutura do Projeto e Funcionalidades

O projeto é composto por três arquivos principais no frontend:

### 1. `index.html`
Define a **estrutura e o conteúdo** do álbum.
* **Páginas e Capa:** Contém a marcação HTML de cada folha do álbum, incluindo a capa estilizada e a contracapa com código de barras simulado.
* **Slots das Figurinhas:** Cada página temática possui slots numerados (`#01` a `#30`) com o nome e a breve descrição da função do respectivo personagem.
* **Controles do Usuário:** Interface do botão de controle de som (habilitar/desabilitar) e setas laterais para folhear o álbum manualmente.

### 2. `style.css`
Responsável pelo **design visual premium e animações**.
* **Visual Premium:** Cores escuras e neon inspiradas em um tema cyberpunk/computacional.
* **Efeitos Especiais:** Implementa o efeito visual de *glitch* no título principal da capa, rotação tridimensional nas argolas da esfera tecnológica central e animações de flutuação nos mini-cards.
* **Feedback de Interação:** Estiliza os cursores (`grab` e `grabbing`) e aplica efeitos de hover nos botões de navegação.
* **Efeito de Dobra:** Sombras gradientes nas bordas internas das páginas pares e ímpares, simulando a lombada de um livro real.
* **Animação de Colagem:** A classe `.sticker-img` aplica uma animação de aproximação (`scale`) e opacidade ao inserir uma figurinha, dando a sensação de que ela foi colada fisicamente.

### 3. `app.js`
Garante a **interatividade e conexão com dados externos**.
* **Integração com a API (Backend):** Executa uma requisição assíncrona (`fetch`) para obter os dados das figurinhas a partir do backend (padrão em `http://localhost:8000`). Mapeia os dados e insere as imagens nos slots correspondentes no HTML.
* **Configuração do PageFlip:** Inicializa e customiza o comportamento da biblioteca de folhear, definindo dimensões, velocidade de transição e um sistema personalizado de detecção de gestos (arrastar com o mouse ou tela sensível ao toque).
* **Sintetizador de Áudio:** Implementa uma função baseada na *Web Audio API* que gera ruído branco e aplica filtros dinâmicos de frequência para simular o som realista de folhas de papel passando, sem a necessidade de baixar arquivos pesados de áudio (.mp3).

---

## 🛠️ Como Executar o Projeto

1. **Backend (API):**
   Para preencher as figurinhas automaticamente, garanta que o servidor backend esteja ativo. Navegue até a pasta do backend e execute:
   ```bash
   uvicorn main:app --reload
   ```
   *(Por padrão, a API deve rodar na porta `8000`)*

2. **Frontend:**
   Abra o arquivo `index.html` diretamente em seu navegador ou utilize uma extensão de servidor local (como *Live Server* no VS Code) para visualizar o álbum interativo.
