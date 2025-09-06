"""
API-endepunkter for PAD Framework via FastAPI.
Gir REST-baserte grensesnitt for å samhandle med agentene.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pad.orchestrator import OrchestratorAgent

app = FastAPI(
    title="Polyglot Agentic Developer API",
    description="REST API for PAD-agentrammeverket",
    version="0.1.0"
)
orchestrator = OrchestratorAgent()

class UserRequest(BaseModel):
    prompt: str

class CodeResponse(BaseModel):
    code: str
    feedback: str

@app.post("/generate", response_model=CodeResponse)
def generate_code(request: UserRequest):
    """
    Ta imot brukerprompt og returner generert kode + QA-feedback.
    """
    plan = orchestrator.plan(request.prompt)
    code = orchestrator.codegen_agent.generate_code(plan, orchestrator.context_agent)
    if not code:
        raise HTTPException(status_code=400, detail="Kunne ikke generere kode.")
    feedback = orchestrator.qa_agent.validate_code(code)
    return CodeResponse(code=code, feedback=feedback)
