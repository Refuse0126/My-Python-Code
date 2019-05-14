"""
reloadAll.py:过渡重载。
reload的局限在于，重载模块时，不能连同模块文件中导入的子模块一起重载
采用过渡重载，可以在重载模块时，检测模块内的属性类型，如果为模块类型，则递归
Date:2019.5.14
"""
import types
from imp import reload

def status(module):
    print('reloading '+module.__name__)

def transitive_reload(module,visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module]=None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj,visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg,visited)

if __name__ == '__main__':
    import reloadAll
    reload_all(reloadAll)
