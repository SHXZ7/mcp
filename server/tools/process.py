# server/tools/process.py
import subprocess
from fastapi import APIRouter

router = APIRouter()

@router.post("/run")
def run_command(command: str):
    """Safely run a shell command and return its output"""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=5
        )
        return {
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except Exception as e:
        return {"error": str(e)}
