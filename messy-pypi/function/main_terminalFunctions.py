def DrawChar(x: int, y: int, char: str) -> None:
    print(f"\033[{x};{y}H{char}")