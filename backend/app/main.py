import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from app.models import TransformConfig
from app.orchestration.engine import run_transformation
from app.parsers.text_parser import extract_text_from_files

app = FastAPI(title="Gen AI Content Transformer")

class TransformPayload(BaseModel):
    text: str
    output_types: List[str]
    config: TransformConfig

@app.post("/transform")
async def transform(payload: TransformPayload):
    source = payload.text
    # If you implement file uploads, merge their text into source here
    results = await run_transformation(source, payload.output_types, payload.config.dict())
    return {"results": results}

@app.get("/download/{filename}")
async def download_file(filename: str):
    path = os.path.join("outputs", filename)
    return FileResponse(path, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation")
