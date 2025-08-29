from mcp_client import MCPClient

c = MCPClient("http://localhost:8000")

print("=== FS Tool ===")
print(c.request("http", {
    "method": "POST",
    "url": "http://localhost:8000/tools/fs/read",
    "data": {"path": "README.md"}
}))

print("=== Math Tool ===")
print(c.request("http", {
    "method": "POST",
    "url": "http://localhost:8000/tools/math/eval",
    "data": {"expr": "2+2*5"}
}))

print("=== System Tool ===")
print(c.request("http", {
    "method": "GET",
    "url": "http://localhost:8000/tools/system/info"
}))
