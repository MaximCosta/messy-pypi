import fcntl
import sys
import threading
import os
import termios
import tty
from select import select
import re

escape = {
    "\n": "enter",
    ("\x7f", "\x08"): "backspace",
    ("[A", "OA"): "up",
    ("[B", "OB"): "down",
    ("[D", "OD"): "left",
    ("[C", "OC"): "right",
    "[2~": "insert",
    "[3~": "delete",
    "[H": "home",
    "[F": "end",
    "[5~": "page_up",
    "[6~": "page_down",
    "\t": "tab",
    "[Z": "shift_tab",
    "OP": "f1",
    "OQ": "f2",
    "OR": "f3",
    "OS": "f4",
    "[15": "f5",
    "[17": "f6",
    "[18": "f7",
    "[19": "f8",
    "[20": "f9",
    "[21": "f10",
    "[23": "f11",
    "[24": "f12"
}
mouse_state = {
    # Changer le regex si depacement supperieur a la key  \033[<100;: passer le {1,2} à {1,3}ou+
    # mouse_.._click
    "\033[<0;": "mouse_left_click",
    "\033[<1;": "mouse_middle_click",
    "\033[<2;": "mouse_right_click",
    # mouse_..alt_click
    "\033[<8;": "mouse_left_alt_click",
    "\033[<9;": "mouse_left_alt_click",
    "\033[<10;": "mouse_left_alt_click",
    # mouse_..ctrl_click
    "\033[<16;": "mouse_left_ctrl_click",
    "\033[<17;": "mouse_middle_ctrl_click",
    "\033[<18;": "mouse_right_ctrl_click",
    # mouse_..altctrl_click
    "\033[<24;": "mouse_left_ctrlalt_click",
    "\033[<25;": "mouse_middle_ctrlalt_click",
    "\033[<26;": "mouse_right_ctrlalt_click",
    # mouse_drag_.._click
    "\033[<32;": "mouse_drag_left_click",
    "\033[<33;": "mouse_drag_middle_click",
    "\033[<34;": "mouse_drad_right_click",
    # mouse_drag_..alt_click
    "\033[<40;": "mouse_left_alt_click",
    "\033[<41;": "mouse_left_alt_click",
    "\033[<42;": "mouse_left_alt_click",
    # mouse_drag_..ctrl_click
    "\033[<48;": "mouse_left_ctrl_click",
    "\033[<49;": "mouse_middle_ctrl_click",
    "\033[<50;": "mouse_right_ctrl_click",
    # mouse_drag_..ctrlalt_click
    "\033[<56;": "mouse_left_ctrlalt_click",
    "\033[<57;": "mouse_middle_ctrlalt_click",
    "\033[<58;": "mouse_right_ctrlalt_click",
    # mouse_scroll..
    "\033[<64;": "mouse_scroll_up",
    "\033[<65;": "mouse_scroll_down",
    # mouse_scroll_alt..
    "\033[<72;": "mouse_scroll_alt_up",
    "\033[<73;": "mouse_scroll_alt_down",
    # mouse_scroll_ctrl..
    "\033[<80;": "mouse_scroll_ctrl_up",
    "\033[<81;": "mouse_scroll_ctrl_down",
    # mouse_scroll_ctrlalt..
    "\033[<88;": "mouse_scroll_ctrl_up",
    "\033[<89;": "mouse_scroll_ctrl_down",
}
new = threading.Event()
idle = threading.Event()
mouse_move = threading.Event()
mouse_report: bool = False
idle.set()
stopping: bool = False
started: bool = False
reader: threading.Thread

def start(cls):
    cls.stopping = False
    cls.reader = threading.Thread(target=cls._get_key)
    cls.reader.start()
    cls.started = True


def stop(cls):
    if cls.started and cls.reader.is_alive():
        cls.stopping = True
        try:
            cls.reader.join()
        except:
            pass


def last(cls) -> str:
    if cls.list:
        return cls.list.pop()
    else:
        return ""


def get(cls) -> str:
    if cls.list:
        return cls.list.pop(0)
    else:
        return ""


def get_mouse(cls):
    if new.is_set():
        new.clear()
    return cls.mouse_pos


def mouse_moved(cls):
    if mouse_move.is_set():
        cls.mouse_move.clear()
        return True
    else:
        return False


def has_key(cls) -> bool:
    return bool(cls.list)


def clear(cls):
    cls.list = []


class Raw(object):
    def __init__(self, stream):
        self.stream = stream
        self.fd = self.stream.fileno()

    def __enter__(self):
        self.original_stty = termios.tcgetattr(self.stream)
        tty.setcbreak(self.stream)

    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.stream, termios.TCSANOW, self.original_stty)


class Nonblocking(object):
    """Set nonblocking mode for device"""

    def __init__(self, stream):
        self.stream = stream
        self.fd = self.stream.fileno()

    def __enter__(self):
        self.orig_fl = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.orig_fl | os.O_NONBLOCK)

    def __exit__(self, *args):
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.orig_fl)


clear = "\033[2J\033[0;0f"  # * Clear screen and set cursor to position 0,0
mouse_on = "\033[?1002h\033[?1015h\033[?1006h"  # * Enable reporting of mouse position on click and release
mouse_off = "\033[?1002l"  # * Disable mouse reporting
mouse_direct_on = "\033[?1003h"  # * Enable reporting of mouse position at any movement
mouse_direct_off = "\033[?1003l"  # * Disable direct mouse reporting


def get_key():
    Lock = True
    input_key = ""
    input_save = ""
    clean_key = ""
    click_state = ""
    liste = [""]
    mouse_pos = (0, 0)

    while Lock:
        with Raw(sys.stdin):
            if not select([sys.stdin], [], [], 0.1)[0]:
                continue
            input_key += sys.stdin.read(1)
            if input_key == "\033":
                with Nonblocking(sys.stdin):
                    input_key += sys.stdin.read(20)
                    if input_key.startswith("\033[<"):
                        _ = sys.stdin.read(1000)
            click_state = ""
            if input_key == "\033":
                clean_key = "escape"
            if not re.search("\x1b\[<[0-9]{1,2};", input_key) == None:
                escape_element = re.search("\x1b\[<[0-9]{1,2};", input_key).group(0)
                if escape_element in mouse_state.keys() and not re.search("\x1b\[<[0-9]{1,2};[0-9]+;[0-9]+[mM]",
                                                                          input_key) == None:
                    regex = re.search("\x1b\[<[0-9]{1,2};([0-9]+);([0-9]+)([mM])", input_key)
                    mouse_pos = (int(regex.group(1)), int(regex.group(2)))
                    click_state = {"m": "up", "M": "down"}[regex.group(3)]
                clean_key = mouse_state[escape_element]
            elif input_key == "\\":
                clean_key = "\\"
            else:
                clean_key = input_key
            if clean_key:
                liste.append(clean_key)
                if len(liste) > 10: del liste[0]
                clean_key = ""
            input_save = input_key
            input_key = ""
            Lock = False

        print(f"{str(liste[-1].encode('utf-8')).center(50)},\t {mouse_pos=},\t {click_state=},\t {input_save=}")


print(mouse_on)
while True:
    get_key()

"""
elif input_key.startswith(("\033[<0;", "\033[<35;", "\033[<64;", "\033[<65;", "\033[<32", "\033[<2;", "\033[<1;","\033[<33")):
	try:
		if input_key.endswith("m"):
			click_state = "up"
		elif input_key.endswith("M"):
			click_state = "down"
		mouse_pos = (int(input_key.split(";")[1]), int(input_key.split(";")[2].rstrip("mM")))
	except:
		pass
	else:
		# if input_key.
		if input_key.startswith("\033[<35;"):		#* Detected mouse move in mouse direct mode
			mouse_move.set()
			new.set()
		elif input_key.startswith("\033[<64;"):		#* Detected mouse scroll up
			clean_key = "mouse_scroll_up"
		elif input_key.startswith("\033[<65;"):		#* Detected mouse scroll down
			clean_key = "mouse_scroll_down"
		elif input_key.startswith("\033[<32;"):
			clean_key = "mouse_drag"
		elif input_key.startswith("\033[<2;"):
			clean_key = "mouse_left_click"
		elif input_key.startswith("\033[<33;"):
			clean_key = "mouse_middle_drag"
		elif input_key.startswith("\033[<1;"):
			clean_key = "mouse_middle_click"
		elif input_key.startswith("\033[<0;") and input_key.endswith("m"): #* Detected mouse click release
			for key_name, positions in mouse.items(): #* Check if mouse position is clickable
				if list(mouse_pos) in positions:
					clean_key = key_name
					break
			else:
				clean_key = "mouse_click"
"""
