from pad.api import app  # FastAPI-app for REST API
from pad.orchestrator import OrchestratorAgent

if __name__ == "__main__":
    import sys
    if "--api" in sys.argv:
        import uvicorn
        uvicorn.run("pad.api:app", host="0.0.0.0", port=8000, reload=True)
    else:
        orchestrator = OrchestratorAgent()
        orchestrator.run()
