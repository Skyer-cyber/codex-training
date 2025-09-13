import os
from typing import List

HISTORY_FILE = os.environ.get(
    "CALC_HISTORY_FILE",
    os.path.join(os.path.dirname(__file__), "history.log"),
)


def _record(operation: str, a: float, b: float, result: float) -> None:
    symbol_map = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
    symbol = symbol_map.get(operation, operation)
    entry = f"{a} {symbol} {b} = {result}"
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def get_history() -> List[str]:
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def add(a: float, b: float) -> float:
    result = a + b
    _record("add", a, b, result)
    return result


def subtract(a: float, b: float) -> float:
    result = a - b
    _record("subtract", a, b, result)
    return result


def multiply(a: float, b: float) -> float:
    result = a * b
    _record("multiply", a, b, result)
    return result


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("不能除以零")
    result = a / b
    _record("divide", a, b, result)
    return result


def calculate(operation: str, a: float, b: float) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        raise ValueError(f"不支持的操作: {operation}")
    return operations[operation](a, b)
