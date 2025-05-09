import uvicorn
import sys

if __name__ == "__main__":
    """ 服务启动入口 """
    reload = True
    if sys.platform.startswith("win"):
        reload = False
    uvicorn.run(
        "src.api.app:start",
        host="0.0.0.0",
        port=8888,
        reload=reload,
        log_level="info",
    )
