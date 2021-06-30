import fcntl
import sys
import threading
import os
import termios
import tty
from select import select

mouse = {}
mouse_pos = (0, 0)
escape = {
	"\n" :					"enter",
	("\x7f", "\x08") :		"backspace",
	("[A", "OA") :			"up",
	("[B", "OB") :			"down",
	("[D", "OD") :			"left",
	("[C", "OC") :			"right",
	"[2~" :					"insert",
	"[3~" :					"delete",
	"[H" :					"home",
	"[F" :					"end",
	"[5~" :					"page_up",
	"[6~" :					"page_down",
	"\t" :					"tab",
	"[Z" :					"shift_tab",
	"OP" :					"f1",
	"OQ" :					"f2",
	"OR" :					"f3",
	"OS" :					"f4",
	"[15" :					"f5",
	"[17" :					"f6",
	"[18" :					"f7",
	"[19" :					"f8",
	"[20" :					"f9",
	"[21" :					"f10",
	"[23" :					"f11",
	"[24" :					"f12"
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
	if cls.list: return cls.list.pop()
	else: return ""
def get(cls) -> str:
	if cls.list: return cls.list.pop(0)
	else: return ""
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

clear				= "\033[2J\033[0;0f"					#* Clear screen and set cursor to position 0,0
mouse_on			= "\033[?1002h\033[?1015h\033[?1006h" 	#* Enable reporting of mouse position on click and release
mouse_off			= "\033[?1002l" 						#* Disable mouse reporting
mouse_direct_on		= "\033[?1003h"							#* Enable reporting of mouse position at any movement
mouse_direct_off	= "\033[?1003l"							#* Disable direct mouse reporting

input_key = ""
clean_key = ""
click_state = ""
liste = [""]
print(mouse_on)
while True:
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
		elif input_key == "\\":
			clean_key = "\\"
		else:
			clean_key = input_key
		if clean_key:
			liste.append(clean_key)
			if len(liste) > 10: del liste[0]
			clean_key = ""
		input_key = ""


	print(fr"{liste[-1]=}, {mouse_pos=}, {mouse_move.is_set()=}, {click_state=}")
