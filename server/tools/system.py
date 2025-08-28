import platform, psutil
from fastapi import APIRouter

router = APIRouter()

@router.get("/system/info")
def system_info():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "cpu_count": psutil.cpu_count(),
        "memory": psutil.virtual_memory()._asdict(),
    }
