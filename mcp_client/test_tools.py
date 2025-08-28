from mcp_client import MCPClient

c = MCPClient()

# Read a file
print(c.request("http", {
    "url": "http://localhost:8000/tools/fs/read",
    "path": "README.md"
}))

# Run math
print(c.request("http", {
    "url": "http://localhost:8000/tools/math/eval",
    "expr": "math.sqrt(16)"
}))

# System info
print(c.request("http", {
    "url": "http://localhost:8000/tools/system/info"
}))
