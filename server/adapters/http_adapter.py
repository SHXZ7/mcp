import httpx
from typing import Dict, Any

class HttpAdapter:
    name = "http"

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        url = input.get("url")
        method = input.get("method", "GET").upper()
        headers = input.get("headers", {})
        data = input.get("data")

        if not url:
            return {"error": "Missing 'url' field"}

        async with httpx.AsyncClient(timeout=10) as client:
            try:
                response = await client.request(method, url, headers=headers, json=data)
                return {
                    "status": response.status_code,
                    "headers": dict(response.headers),
                    "body": response.text[:500]  # truncate for safety
                }
            except Exception as e:
                return {"error": str(e)}
