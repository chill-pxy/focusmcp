from mcp.server.fastmcp import FastMCP
import ctypes

mcp = FastMCP("FocusTool")

@mcp.tool()

def focusFunc():
    """focus function test"""
    lib = ctypes.CDLL('C:\\project\\FOCUS\\build\\x64-Debug\\bin/engine.dll')
    lib.getSceneObjCount.restype = int
    #lib.getSceneObjCount.argtypes = [ctypes.c_int]
    res = lib.getSceneObjCount()
    print(res)
    return res

if __name__ == "__main__":
    mcp.run(transport='stdio')