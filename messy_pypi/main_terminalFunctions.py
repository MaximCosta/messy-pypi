import os
import time


def print_char(x: int, y: int, char: str) -> None:
    """
    x: >
    y: \\/
    """
    print(f"\033[{y};{x}H{char}")


def clear() -> None:
    # os.system("cls||clear")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def terminal_size(item: str = None) -> (tuple[int, int] or int):
    """
    X: >
    Y: \\/
    """
    size = os.get_terminal_size()
    if item is None:
        return size[0], size[1]
    elif item == "X":
        return size[0]
    elif item == "Y":
        return size[1]


def message_page_trop_petite(sizex, sizey) -> bool:
    """
    sizex, sizey: int
    """
    if sizex > terminal_size("X") or sizey > terminal_size("Y"):
        print("Trop petit")
        time.sleep(.50)
        return True
    return False
