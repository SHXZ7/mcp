from mcp_client import MCPClient

client = MCPClient("http://localhost:8000")

print("=== HTTP GET ===")
print(client.call_tool("http/get", {"action": "get", "url": "https://api.github.com"}))

print("=== HTTP POST ===")
print(client.call_tool("http/post", {"action": "post", "url": "https://httpbin.org/post", "data": {"msg": "Hello MCP"}}))
