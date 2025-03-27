from mcp.server.fastmcp import FastMCP
import ctypes

mcp = FastMCP("FocusTool")
lib = ctypes.CDLL('C:\\project\\FOCUS\\build\\x64-Debug\\bin/engine.dll')

@mcp.tool(name="runEngine")
def runEngine():
    """run FOCUS engine"""
    lib.run()

@mcp.tool(name="countObj")
def countObj():
    """count obj sums in FOCUS engine"""
    lib.getSceneObjCount.restype = ctypes.c_int
    return lib.getSceneObjCount()

@mcp.tool(name="plantObj")
def countObj():
    """plant obj in FOCUS engine"""
    lib.plantObj()

if __name__ == "__main__":
    mcp.run(transport='stdio')