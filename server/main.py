from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
from .adapters import adapters

app = FastAPI(title="MCP Server", version="0.1")

class MCPRequest(BaseModel):
    version: str
    intent: str
    tool: dict

@app.post("/requests")
async def handle_request(req: MCPRequest):
    tool_name = req.tool.get("name")
    adapter = adapters.get(tool_name)

    if not adapter:
        raise HTTPException(status_code=400, detail=f"Unknown tool: {tool_name}")

    result = await adapter.run(req.tool.get("input", {}))

    return {
        "request_id": str(uuid.uuid4()),
        "tool": tool_name,
        "result": result
    }
