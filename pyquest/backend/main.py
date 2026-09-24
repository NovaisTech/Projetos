from fastapi import FastAPI

app = FastAPI(title="PyQuest API")

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
    return [
        {
            "id":1,
            "badge": "Lv 1",
            "titulo": "Your first program syntax",
            "tarefas": 18,
            "dificuldade": "Beginner",
            "desbloqueado": True
        },
        
        {
            "id": 2,
            "badge": "Lv 2",
            "titulo": "Data types and control flow",
            "tarefas": 55,
            "dificuldade":"Beginner",
            "esbloqueado": False
        },
        
        {
            "id": 3,
            "badge": "Lv 3",
            "titulo": "Strings, collectiosn, loops",
            "tarefas": "Intermediate",
            "desbloqueado": False            
            
        }
        
        
    ]
        