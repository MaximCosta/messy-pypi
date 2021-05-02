import os

def DrawChar(x: int, y: int, char: str) -> None:
    """
    x: >
    y: \/
    """
    print(f"\033[{y};{x}H{char}")

def Clear() -> None:
    os.system("cls||clear")

def TerminalSize(item: str=None) -> (tuple[int, int] or int):
    """
    X: >
    Y: \/
    """
    size = os.get_terminal_size()
    match item:
        case None:
            return size[0], size[1]
        case "X":
            return size[0]
        case "Y":
            return size[1]

def MessageTropPetitPage(size) -> bool:
    """
    size: (int, int)
    """
    if size > TerminalSize("X") or size > TerminalSize("Y"):
        print("Trio ptit")
        return True
    return False