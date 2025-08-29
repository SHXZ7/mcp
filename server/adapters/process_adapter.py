import subprocess
from typing import Dict, Any

class ProcessAdapter:
    name = "process"

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        command = input.get("command")
        
        if not command:
            return {"error": "Missing 'command' field"}
        
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            return {
                "status": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except subprocess.TimeoutExpired:
            return {"error": "Command timed out"}
        except Exception as e:
            return {"error": str(e)}
