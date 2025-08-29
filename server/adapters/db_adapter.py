import sqlite3
from typing import Dict, Any

class DbAdapter:
    name = "db"

    async def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        query = input.get("query")
        db_path = input.get("db_path", "example.db")
        
        if not query:
            return {"error": "Missing 'query' field"}
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            
            if query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                conn.close()
                return {"columns": columns, "rows": rows}
            else:
                conn.commit()
                conn.close()
                return {"status": "success", "rowcount": cursor.rowcount}
                
        except Exception as e:
            return {"error": str(e)}
