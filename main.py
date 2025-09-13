import argparse
from src.calculator import calculate, get_history


def main() -> None:
    parser = argparse.ArgumentParser(description="简单的命令行计算器")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide", "history"],
        help="要执行的操作",
    )
    parser.add_argument("a", type=float, nargs="?", help="第一个数字")
    parser.add_argument("b", type=float, nargs="?", help="第二个数字")
    args = parser.parse_args()

    if args.operation == "history":
        for entry in get_history():
            print(entry)
        return

    if args.a is None or args.b is None:
        parser.error("执行运算需要提供两个数字")

    try:
        result = calculate(args.operation, args.a, args.b)
    except ValueError as exc:
        parser.exit(message=str(exc) + "\n")
    print(result)


if __name__ == "__main__":
    main()
