from typing import Dict, Any

class NoOpAdapter:
    name = "noop"

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return {"ok": True, "input": input}
