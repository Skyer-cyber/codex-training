# 我的第一个Codex训练项目
print("欢迎使用Codex!")

def calculator(a, b, operation):
    """简单的计算器函数"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "错误：不能除以零"
    else:
        return "不支持的操作"

# 测试代码
print("测试计算器:")
print(f"10 + 5 = {calculator(10, 5, 'add')}")
print(f"10 - 3 = {calculator(10, 3, 'subtract')}")
print(f"4 * 6 = {calculator(4, 6, 'multiply')}")
print(f"15 / 3 = {calculator(15, 3, 'divide')}")
