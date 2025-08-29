import requests
from typing import Any, Dict, Optional
import httpx
import asyncio

class MCPClientError(Exception):
    pass

class MCPClient:
    """Synchronous MCP client using requests."""
    def __init__(self, base_url: str = "http://localhost:8000", timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _payload(self, tool: str, input_data: Optional[Dict[str, Any]] = None, intent: str = "execute", version: str = "mcp-0.1"):
        return {
            "version": version,
            "intent": intent,
            "tool": {
                "name": tool,
                "input": input_data or {}
            }
        }

    def request(self, tool: str, input_data: Optional[Dict[str, Any]] = None, intent: str = "execute") -> Dict[str, Any]:
        payload = self._payload(tool, input_data, intent)
        url = f"{self.base_url}/requests"
        try:
            r = requests.post(url, json=payload, timeout=self.timeout)
        except Exception as e:
            raise MCPClientError(f"Network error when calling {url}: {e}") from e
        if r.status_code >= 400:
            try:
                detail = r.json()
            except Exception:
                detail = r.text
            raise MCPClientError(f"Server returned {r.status_code}: {detail}")
        try:
            return r.json()
        except Exception as e:
            raise MCPClientError(f"Failed to parse JSON response: {e}; raw={r.text}") from e

    def call_tool(self, tool: str, input_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Convenience method that matches the test file expectations."""
        return self.request(tool, input_data)


class AsyncMCPClient:
    """Async MCP client using httpx.AsyncClient."""
    def __init__(self, base_url: str = "http://localhost:8000", timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _payload(self, tool: str, input_data: Optional[Dict[str, Any]] = None, intent: str = "execute", version: str = "mcp-0.1") -> Dict[str, Any]:
        return {
            "version": version,
            "intent": intent,
            "tool": {
                "name": tool,
                "input": input_data or {}
            }
        }

    async def request(self, tool: str, input_data: Optional[Dict[str, Any]] = None, intent: str = "execute") -> Dict[str, Any]:
        payload = self._payload(tool, input_data, intent)
        url = f"{self.base_url}/requests"
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                r = await client.post(url, json=payload)
        except Exception as e:
            raise MCPClientError(f"Network error when calling {url}: {e}") from e
        if r.status_code >= 400:
            try:
                detail = r.json()
            except Exception:
                detail = r.text
            raise MCPClientError(f"Server returned {r.status_code}: {detail}")
        try:
            return r.json()
        except Exception as e:
            raise MCPClientError(f"Failed to parse JSON response: {e}; raw={r.text}") from e

    async def call_tool(self, tool: str, input_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Convenience method that matches the test file expectations."""
        return await self.request(tool, input_data)

# small convenience function for interactive use
def quick_test_sync(base_url: str = "http://localhost:8000") -> None:
    """Prints the sample payload and attempts a request (wrapped in try/except)."""
    c = MCPClient(base_url)
    sample = c._payload("http", {"url": "https://jsonplaceholder.typicode.com/todos/1"}, intent="fetch")
    print("Sample payload to be sent:\n", sample)
    print("Attempting to call the MCP server...")
    try:
        resp = c.request("http", {"url": "https://jsonplaceholder.typicode.com/todos/1"}, intent="fetch")
        print("Response from server:\n", resp)
    except MCPClientError as e:
        print("MCPClientError:", e)
