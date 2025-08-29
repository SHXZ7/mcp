# server/tools/http_tool.py
import requests
from fastapi import APIRouter

router = APIRouter()

@router.post("/tools/http/get")
async def http_get(url: str):
    try:
        resp = requests.get(url, timeout=10)
        return {"status": resp.status_code, "headers": dict(resp.headers), "body": resp.text[:500]}
    except Exception as e:
        return {"error": str(e)}

@router.post("/tools/http/post")
async def http_post(url: str, data: dict):
    try:
        resp = requests.post(url, json=data, timeout=10)
        return {"status": resp.status_code, "headers": dict(resp.headers), "body": resp.text[:500]}
    except Exception as e:
        return {"error": str(e)}
