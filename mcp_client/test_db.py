from mcp_client import MCPClient

client = MCPClient("http://localhost:8000")

print("=== DB Tool ===")
print(client.call_tool("db/query", {"query": "CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT);"}))
print(client.call_tool("db/query", {"query": "INSERT INTO users (id, name) VALUES (1, 'Alice');"}))
print(client.call_tool("db/query", {"query": "SELECT * FROM users;"}))
