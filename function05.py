a = 12

globalVariable = locals()
print("全局作用域", globalVariable)


# 全局作用域 {'__name__': '__main__',
# '__doc__': None,
# '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020CF5AC2FD0>,
# '__spec__': None,
# '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'D:\\dev\\Python\\pyCharmWorkspace\\PythonBasic\\function05.py',
# '__cached__': None,
# 'a': 12,
# 'globalVariable': {...}}

def test():
    b = 23
    localVariable = locals()
    print("函数作用域", localVariable)
    return b


test()  # 函数作用域 {'b': 23}
