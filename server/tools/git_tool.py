# server/tools/git_tool.py
import subprocess
from fastapi import APIRouter

router = APIRouter()

def run_git_command(args):
    try:
        result = subprocess.run(
            ["git"] + args, capture_output=True, text=True, timeout=10
        )
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}
    except Exception as e:
        return {"error": str(e)}

@router.post("/tools/git/status")
async def git_status():
    return run_git_command(["status"])

@router.post("/tools/git/branches")
async def git_branches():
    return run_git_command(["branch", "--list"])

@router.post("/tools/git/logs")
async def git_logs(limit: int = 5):
    return run_git_command(["log", f"-{limit}", "--oneline"])
