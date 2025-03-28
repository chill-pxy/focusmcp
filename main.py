from mcp.server.fastmcp import FastMCP
import ctypes

mcp = FastMCP("FocusTool")
lib = ctypes.CDLL('E:\\project\\FOCUS\\build\\x64-Debug\\bin/engine.dll')

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
def plantObj(path: str):
    """plant obj with path in FOCUS engine"""
    lib.plantObj.argtypes = [ctypes.c_char_p]
    lib.plantObj(path.encode('utf-8'))

@mcp.tool(name="getModelPathList")
def plantObj():
    """get all model path by a list"""
    lib.getModelPathList.restype = ctypes.c_char_p
    return lib.getModelPathList()

@mcp.tool(name="changeObjPosition")
def changeObjPosition(objname: str, x:float, y:float, z:float):
    """change obj position with name by x y z coordinate"""
    lib.changeObjPosition.argtypes = [ctypes.c_char_p, float, float, float]
    lib.changObjPosition(objname, x, y, z)

@mcp.tool(name="changeObjScale")
def changeObjScale(objname: str, x:float, y:float, z:float):
    """change obj scale with name by x y z value"""
    lib.changeObjScale.argtypes = [ctypes.c_char_p, float, float, float]
    lib.changObjScale(objname, x, y, z)

if __name__ == "__main__":
    mcp.run(transport='stdio')
