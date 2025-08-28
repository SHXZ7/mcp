"""
mcp_client - minimal Python SDK for talking to a local MCP server.

Usage:
    from mcp_client import MCPClient, AsyncMCPClient

    # sync
    client = MCPClient("http://localhost:8000")
    resp = client.request(tool="http", input_data={"url": "https://jsonplaceholder.typicode.com/todos/1"})
    print(resp)

    # async (requires an async environment)
    import asyncio
    async def a():
        client = AsyncMCPClient("http://localhost:8000")
        resp = await client.request("http", {"url": "https://jsonplaceholder.typicode.com/todos/1"})
        print(resp)
    asyncio.run(a())
"""
from .client import MCPClient, MCPClientError, AsyncMCPClient
__all__ = ["MCPClient", "MCPClientError", "AsyncMCPClient"]
