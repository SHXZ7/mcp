import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ReadFileRequest(BaseModel):
    path: str

class WriteFileRequest(BaseModel):
    path: str
    content: str

class ListFilesRequest(BaseModel):
    path: str = "."

@router.post("/fs/read")
def read_file(req: ReadFileRequest):
    if not os.path.exists(req.path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(req.path, "r", encoding="utf-8") as f:
        return {"path": req.path, "content": f.read()}

@router.post("/fs/write")
def write_file(req: WriteFileRequest):
    with open(req.path, "w", encoding="utf-8") as f:
        f.write(req.content)
    return {"status": "success", "path": req.path}

@router.post("/fs/list")
def list_files(req: ListFilesRequest):
    if not os.path.isdir(req.path):
        raise HTTPException(status_code=400, detail="Not a directory")
    return {"path": req.path, "files": os.listdir(req.path)}
