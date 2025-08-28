from typing import Protocol, Dict, Any

class ToolAdapter(Protocol):
    name: str

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        ...
