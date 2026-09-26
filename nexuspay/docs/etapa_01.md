# 📘 NexusPay — Diário de Bordo & Documentação Técnica

## Etapa 1: Fundação, Arquitetura e Inicialização do Servidor Central

---

### 1. Visão Geral do Projeto

O **NexusPay** é uma plataforma distribuída de vendas e recargas inspirada no modelo de bilhetagem eletrônica de transporte público (como o sistema de recarga do Bilhete Único em São Paulo).

```
                        ┌──────────────────────────────────────────┐
                        │       CONCENTRADOR CENTRAL (MATRIZ)      │
                        │  - FastAPI na porta 8000                 │
                        │  - Painel Admin & Kill Switch            │
                        │  - Banco Consolidado (PostgreSQL)        │
                        └─────────────────────┬────────────────────┘
                                              │ (HTTP / Webhooks)
                     ┌────────────────────────┴────────────────────────┐
                     ▼                                                 ▼
     ┌───────────────────────────────┐                 ┌───────────────────────────────┐
     │   TERMINAL CLIENTE 1 (LOCAL)  │                 │   TERMINAL CLIENTE 2 (LOCAL)  │
     │ - Ponto de Venda / Totem      │                 │ - Ponto de Venda / Totem      │
     │ - Banco Local Resiliente (DB) │                 │ - Banco Local Resiliente (DB) │
     └───────────────────────────────┘                 └───────────────────────────────┘
```

A premissa central é o aprendizado prático e profundo de **arquitetura de software**, **APIs assíncronas**, **sincronização de borda (edge/offline-first)** e **segurança**, com **custo zero** de infraestrutura.

---

### 2. Linha do Tempo da Sessão e Passos Executados

#### Passo 1: O "Escudo de Segurança" (`.gitignore`)

Iniciamos garantindo que nenhuma informação sigilosa (chaves de API, senhas, bancos de dados locais `.db`, arquivos de cache `__pycache__` ou ambientes virtuais `venv`) seja enviada para a internet.

![Criação do .gitignore no VS Code](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790393901940.png)

- **O que foi feito:** Criação do arquivo `.gitignore` com 24 linhas de regras de exclusão.
- **Conceito:** Proteção ativa contra vazamento de credenciais e poluição do histórico de commits.

---

#### Passo 2: Adequação ao Monorepo da NovaisTech

Identificamos que o repositório principal no GitHub já é `NovaisTech / Projetos`, atuando como um monorepo/oficina com múltiplos projetos (como o `pyquest`).

![Repositório Monorepo NovaisTech no GitHub](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790395761541.png)

- **Diagnóstico:** O comando `git init` anterior havia criado um `.git` isolado dentro da subpasta.
- **Ação Corretiva:** Removemos o controle interno (`Remove-Item -Recurse -Force .git`) para que a pasta mãe gerencie todo o histórico sem conflito de submódulos.

![Resolução do Git Interno](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790396121511.png)

---

#### Passo 3: Padronização de Nomenclatura e Abertura no VS Code

A pasta original se chamava `Rede de Vendas` (com espaços e maiúsculas). Para seguir o padrão do mercado e harmonizar com `pyquest`:

1. Fechamos o bloqueio de arquivo do Windows.
2. Renomeamos a pasta para `nexuspay`.
3. Abrimos a pasta mãe `Projetos` no VS Code.

![Visualização Unificada dos Projetos](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790397309893.png)

---

#### Passo 4: Isolamento com Ambiente Virtual (`venv`)

Criamos um laboratório Python exclusivo para o `nexuspay` para não misturar versões de bibliotecas globais da máquina.

![Ambiente Virtual venv Criado e Ativado](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790397668209.png)

- **Comandos:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **Indicador visual:** O prefixo `(venv)` em verde no terminal confirma a ativação.

---

#### Passo 5: Manifesto de Dependências (`requirements.txt`)

Declaramos formalmente os pacotes necessários para o ecossistema assíncrono:

![Criação do requirements.txt](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790398145295.png)

- `fastapi>=0.110.0` — Framework web assíncrono de alto desempenho.
- `uvicorn[standard]>=0.28.0` — Servidor ASGI para processamento de conexões de rede.
- `httpx>=0.27.0` — Cliente HTTP assíncrono para comunicação entre servidores.
- `pydantic>=2.6.0` — Validação estrita e modelagem de tipos de dados.

Instalamos tudo no `venv` via `pip install -r requirements.txt`:

![Instalação das Bibliotecas via pip](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790398192671.png)

---

#### Passo 6: Criação dos Módulos e Código do Servidor Central

Criamos a estrutura modular com três pilares:

```powershell
mkdir concentrador, terminal_cliente, simulador
```

Criamos o arquivo `concentrador/main.py`:

```python
from fastapi import FastAPI

app = FastAPI(
    title="NexusPay — Concentrador Central",
    description="API Centralizadora para gestão de terminais e consolidação de vendas.",
    version="1.0.0"
)

@app.get("/")
async def rota_raiz():
    return {
        "sistema": "NexusPay Concentrador",
        "status": "online",
        "mensagem": "Servidor Central operacional"
    }

@app.get("/health")
async def checagem_saude():
    return {"status": "ok", "servico": "concentrador"}
```

---

#### Passo 7: Debugging — O Aprendizado do _Working Directory_

Ao tentar iniciar o servidor inicialmente de dentro da pasta `concentrador`, o Python gerou `ModuleNotFoundError: No module named 'concentrador'`:

![Erro de Importação do Módulo](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790400485306.png)

- **Diagnóstico de Engenharia:** Como o terminal já estava em `...\nexuspay\concentrador`, a instrução `concentrador.main:app` procurava uma pasta duplicada.
- **Solução de Arquitetura:** Voltamos para a raiz do projeto com `cd ..` (`...\nexuspay`) para que todos os módulos sejam resolvidos a partir de um ponto único.

---

#### Passo 8: Servidor Central Operacional!

Executamos o comando com recarregamento em tempo real:

```powershell
uvicorn concentrador.main:app --reload --port 8000
```

![Servidor Uvicorn e FastAPI Ativos](C:/Users/USUÁRIO/.gemini/antigravity/brain/c18eb910-baf1-4a4a-b24d-259e3b5a1297/.user_uploaded/media_1790400774753.png)

> **Resultado:** Servidor Uvicorn ouvindo na porta 8000 (`http://127.0.0.1:8000`), com Swagger interativo disponível em `http://127.0.0.1:8000/docs`.

---

### 3. Conceitos-Chave Fixados Nesta Sessão

1. **Monorepo:** Manter múltiplos projetos interdependentes sob um mesmo repositório Git simplifica o portfólio e a governança.
2. **Ambiente Virtual (`venv`):** Isolamento de dependências para prevenir quebra de código entre projetos diferentes.
3. **ASGI vs WSGI:** O Uvicorn roda sobre ASGI (_Asynchronous Server Gateway Interface_), permitindo lidar com conexões persistentes e assíncronas, crucial para transações de alta frequência.
4. **Decoradores e Rotas (`@app.get`):** Padrão de projeto que associa uma URL e um método HTTP diretamente a uma função de negócio.
5. **Health Checks:** Padrão arquitetural indispensável em computação em nuvem para monitoramento autônomo de disponibilidade.

---

### 4. Próxima Etapa (Sessão 2)

- Criar a aplicação do **Terminal Cliente (Ponto de Venda/Totem)**.
- Configurar o banco de dados local leve (**SQLite**) no cliente para vendas offline.
- Criar a primeira rota de registro de recarga e testar a comunicação entre o Terminal e a Matriz.
