from mcp_client import MCPClient

client = MCPClient("http://localhost:8000")

print("=== Git Status ===")
print(client.call_tool("git/status", {"action": "status"}))

print("=== Git Branches ===")
print(client.call_tool("git/branches", {"action": "branches"}))

print("=== Git Logs ===")
print(client.call_tool("git/logs", {"action": "logs", "limit": 3}))
