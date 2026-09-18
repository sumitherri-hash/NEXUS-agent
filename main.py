from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NEXUS AI Agent")

class AgentRequest(BaseModel):
    player_message: str
    world_state: dict = {}

@app.get("/")
def home():
    return {
        "agent": "NEXUS AI",
        "status": "online"
    }

@app.post("/agent")
def agent(request: AgentRequest):
    return {
        "agent": "NEXUS AI",
        "thought": "Processing player request",
        "action": "observe",
        "message": f"I received: {request.player_message}"
    }
