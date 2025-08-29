import subprocess
from typing import Dict, Any

class GitAdapter:
    name = "git"

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        action = input.get("action")
        
        try:
            if action == "status":
                result = subprocess.run(["git", "status", "--porcelain"], 
                                      capture_output=True, text=True, timeout=10)
                return {"status": result.returncode, "output": result.stdout, "error": result.stderr}
            
            elif action == "branches":
                result = subprocess.run(["git", "branch", "-a"], 
                                      capture_output=True, text=True, timeout=10)
                return {"status": result.returncode, "output": result.stdout, "error": result.stderr}
            
            elif action == "logs":
                limit = input.get("limit", 5)
                result = subprocess.run(["git", "log", f"--max-count={limit}", "--oneline"], 
                                      capture_output=True, text=True, timeout=10)
                return {"status": result.returncode, "output": result.stdout, "error": result.stderr}
            
            else:
                return {"error": f"Unknown git action: {action}"}
                
        except subprocess.TimeoutExpired:
            return {"error": "Git command timed out"}
        except Exception as e:
            return {"error": str(e)}
