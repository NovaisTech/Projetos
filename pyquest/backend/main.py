from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="PyQuest API")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],                          # Permite requisições vindas do navegador
  allow_credentials=True,                
  allow_methods=["*"],                          # Permite métodos GET, POST, etc
  allow_headers=["*"],
  
)


@app.get("/api/status")
def checar_status():

    return {
        "status": "online",
        "jogo": "PyQuest",
        "fase_atual": 1,
        "mensagem": "Servidor do PyQuest operando com sucesso!"
    }


@app.get("/api/levels")
def listar_niveis():
    """Retorna o currículo das fases inspirado na imagem do jogo."""
    return [
        {
            "id": 1,
            "badge": "Lv 1",
            "cor_badge": "#2563EB",  # Azul
            "icone": "💻",
            "titulo": "Seu primeiro programa e sintaxe",
            "tarefas": 18,
            "dificuldade": "Iniciante",
            "desbloqueado": True
        },
        {
            "id": 2,
            "badge": "Lv 2",
            "cor_badge": "#16A34A",  # Verde
            "icone": "📄",
            "titulo": "Tipos de dados e fluxo de controle",
            "tarefas": 55,
            "dificuldade": "Iniciante",
            "desbloqueado": False
        },
        {
            "id": 3,
            "badge": "Lv 3",
            "cor_badge": "#EA580C",  # Laranja
            "icone": "{ }",
            "titulo": "Strings, coleções, loops",
            "tarefas": 61,
            "dificuldade": "Intermediário",
            "desbloqueado": False
        },
        {
            "id": 4,
            "badge": "Lv 4",
            "cor_badge": "#9333EA",  # Roxo
            "icone": "⚙️",
            "titulo": "Funções, decoradores, classes",
            "tarefas": 41,
            "dificuldade": "Intermediário",
            "desbloqueado": False
        }
    ]