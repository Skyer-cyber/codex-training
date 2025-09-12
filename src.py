def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算 - 这里有个小bug等待修复"""
    return a + b  # 故意写错，用于练习调试

def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("不能除以零")
    return a / b
