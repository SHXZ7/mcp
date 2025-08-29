import httpx
from typing import Dict, Any

class HttpToolAdapter:
    name = "http_tool"

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        action = input.get("action")
        url = input.get("url")
        
        if not url:
            return {"error": "Missing 'url' field"}
        
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                if action == "get":
                    response = await client.get(url)
                elif action == "post":
                    data = input.get("data", {})
                    response = await client.post(url, json=data)
                else:
                    return {"error": f"Unknown HTTP action: {action}"}
                
                return {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "body": response.text[:1000]  # truncate for safety
                }
        except Exception as e:
            return {"error": str(e)}
