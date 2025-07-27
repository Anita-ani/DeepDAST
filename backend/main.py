from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from scanner import run_zap_scan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "DeepDAST API is running"}

@app.post("/scan")
async def scan_url(url: str = Form(...)):
    result = run_zap_scan(url)
    return JSONResponse(content=result)
