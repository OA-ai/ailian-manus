from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def startup():
    """ 创建 FastAPI APP """

    app = FastAPI(
        title="Ailian-LangManus API",
        description="API for Ailian-LangManus LangGraph-based agent workflow",
        version="0.0.1",
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
