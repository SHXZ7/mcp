import math
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/math/eval")
def eval_expr(expr: str):
    try:
        # Restrict builtins, allow only math module
        allowed = {"__builtins__": {}, "math": math}
        result = eval(expr, allowed)
        return {"expr": expr, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
