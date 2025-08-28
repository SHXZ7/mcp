from mcp_client import MCPClient, AsyncMCPClient, MCPClientError
import asyncio

def sync_example():
    client = MCPClient("http://localhost:8000")
    try:
        resp = client.request("http", {"url": "https://jsonplaceholder.typicode.com/todos/1"}, intent="fetch")
        print("SYNC response:", resp)
    except MCPClientError as e:
        print("SYNC error:", e)

async def async_example():
    client = AsyncMCPClient("http://localhost:8000")
    try:
        resp = await client.request("http", {"url": "https://jsonplaceholder.typicode.com/todos/1"}, intent="fetch")
        print("ASYNC response:", resp)
    except MCPClientError as e:
        print("ASYNC error:", e)

if __name__ == "__main__":
    print("Running sync example (will fail if your MCP server is not running):")
    sync_example()
    print("\nRunning async example (will fail if your MCP server is not running):")
    asyncio.run(async_example())
