from mcp_client.client import MCPClient

client = MCPClient()

print("=== Process Tool ===")
resp = client.call_tool("process/run", {"command": "echo Hello MCP"})
print(resp)
