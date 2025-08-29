# server/tools/db_tool.py
import sqlite3
from fastapi import APIRouter

router = APIRouter()

DB_PATH = "example.db"

@router.post("/tools/db/query")
async def run_query(query: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return {"query": query, "rows": rows}
    except Exception as e:
        return {"error": str(e)}
