from fastapi import FastAPI

app = FastAPI(
    title="NexusPay - Concentrador Central",
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
