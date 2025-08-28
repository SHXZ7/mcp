import os
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/fs/read")
def read_file(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r", encoding="utf-8") as f:
        return {"path": path, "content": f.read()}

@router.post("/fs/write")
def write_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return {"status": "success", "path": path}

@router.post("/fs/list")
def list_files(path: str = "."):
    if not os.path.isdir(path):
        raise HTTPException(status_code=400, detail="Not a directory")
    return {"path": path, "files": os.listdir(path)}
