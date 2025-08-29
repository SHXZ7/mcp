import math
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class MathRequest(BaseModel):
    expr: str

@router.post("/math/eval")
def eval_expr(req: MathRequest):
    try:
        # Restrict builtins, allow only math module
        allowed = {"__builtins__": {}, "math": math}
        result = eval(req.expr, allowed)
        return {"expr": req.expr, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
