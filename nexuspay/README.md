# 🚀 NexusPay — Rede Distribuída de Vendas e Recargas

O **NexusPay** é uma plataforma distribuída de vendas e recargas inspirada no modelo de bilhetagem eletrônica de transporte público (como o Bilhete Único da cidade de São Paulo).

O sistema opera no modelo **Hub-and-Spoke** (Matriz e Pontos de Venda), suportando operação local resiliente (offline-first), consolidação de transações em tempo real e controle centralizado de status.

---

## 🏗️ Arquitetura do Sistema

- **Concentrador Central (Matriz):**
  - Servidor em **FastAPI** responsável por autenticar terminais, consolidar vendas e gerenciar acessos.
  - Painel Administrativo com métricas financeiras e mecanismo de **Kill Switch** (ativação/desativação remota de terminais).
  - Banco de dados relacional centralizado (**PostgreSQL**).

- **Terminais Locais (Clientes / Pontos de Venda):**
  - Aplicação local em **FastAPI** com interface web para operadores/passageiros.
  - Armazenamento local (**SQLite**) que permite vendas contínuas mesmo sem internet.
  - Mecanismo de sincronização automática e checagem de status (_heartbeat_).

- **Simulador de Demanda:**
  - Script autônomo gerador de transações com modelagem de horários de pico (início da manhã e fim de tarde).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Framework Web:** FastAPI & Uvicorn
- **Bancos de Dados:** SQLite (borda/local) e PostgreSQL (núcleo central)
- **Controle de Versão:** Git & GitHub
