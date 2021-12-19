import re

from main_terminalGetKey import getKey, get_key_bytes
from main_terminalFunctions import print_char, clear, terminal_size, message_page_trop_petite
from random import randint
from re import search
import os


class Functions:
    @classmethod
    def auto_complete(cls, command, list_of_command):
        """
        This function is used to auto-complete the command.
        """
        command_list = []
        for i in list_of_command:
            if i.startswith(command):
                command_list.append(i)
        return command_list

    @classmethod
    def reset_tabulationIndex(cls):
        Draw.reload_all()
        Infos.tabulationIndex = -1


class Draw:
    @classmethod
    def draw_footer(cls):
        x = os.get_terminal_size()[0]
        y = os.get_terminal_size()[1]
        sys.stdout.write(f"\033[{y - 1};0H" + "-" * x)
        sys.stdout.write(f"\033[{y - 1};6H" + Modes.get_mode_name())
        sys.stdout.write(f"\033[{y - 1};20H" + Infos.stack_key)
        sys.stdout.flush()

    @classmethod
    def cursor_key(cls):
        sys.stdout.write(
            f"\033[{Infos.cursor_pos // os.get_terminal_size()[0] + 1};{Infos.cursor_pos % os.get_terminal_size()[0]}H")

    @classmethod
    def actulise_input(cls):
        sys.stdout.write("\033[0;0H" + Infos.input_string + " ")

    @classmethod
    def clear_input(cls):
        sys.stdout.write("\033[0;0H" + " " * os.get_terminal_size()[0])

    @classmethod
    def reload_all(cls):
        clear()
        cls.draw_footer()
        cls.actulise_input()
        cls.cursor_key()


class Config:
    @classmethod
    def load_config(cls):
        """
        This function is used to load the configuration file.
        """
        try:
            with open("config.txt", "r") as f:
                config = f.readlines()
            return config
        except FileNotFoundError:
            print("Configuration file not found.")
            return False

    @classmethod
    def get_history(cls):
        """
        This function is used to get the history of commands.
        """
        try:
            with open("history.txt", "r") as f:
                history = [i.lstrip() for i in f.readlines()]
            return history
        except FileNotFoundError:
            return []

    @classmethod
    def write_history(cls, command):
        """
        This function is used to write the history of commands.
        """
        with open("history.txt", "a") as f:
            f.write(command + "\n")


class Infos:
    stack_key = ""
    input_string = ""
    cursor_pos = 1
    tabulationIndex = -1
    history = Config.get_history()
    history_index = 0


class Modes:
    allModes = []
    currentMode = 0

    def __init__(self, id, name, commands):
        self.modId = id
        self.modName = name
        self.command = commands
        self.allModes.append(self)

    @staticmethod
    def change_mode(new_mode: int):
        if new_mode == 0:
            Modes.currentMode = 0
            Infos.stack_key = ""
        elif new_mode == 1:
            Modes.currentMode = 1
            Functions.reset_tabulationIndex()
        elif new_mode == 2:
            Modes.currentMode = 2
        elif new_mode == 3:
            Modes.currentMode = 3
        Draw.draw_footer()

    def normal_insert_mode(key: str):
        if re.match('\\x1b\\[[A-D]', key):
            if key == "\x1b[C":
                Infos.cursor_pos = min(Infos.cursor_pos + 1, len(Infos.input_string) + 1)
            elif key == "\x1b[D":
                Infos.cursor_pos = max(0, Infos.cursor_pos - 1)
            elif key == "\x1b[A":  # Up
                if Infos.history_index > -len(Infos.history):
                    Infos.history_index = max(Infos.history_index - 1, 0-len(Infos.history))
                    Infos.input_string = Infos.history[Infos.history_index]
                    Infos.cursor_pos = len(Infos.input_string) + 1
                Draw.clear_input()
                Draw.actulise_input()
            elif key == "\x1b[B":  # Down
                if Infos.history_index < -1:
                    Infos.history_index += 1
                    Infos.input_string = Infos.history[Infos.history_index]
                    Infos.cursor_pos = len(Infos.input_string) + 1
                elif Infos.history_index == -1:
                    Infos.history_index = 0
                    Infos.input_string = ""
                    Infos.cursor_pos = 1
                Draw.clear_input()
                Draw.actulise_input()


    def normal_mode(key: str):
        if re.match('^[0-9d hjklwb]$', key) or key in ["\x01", "\x7f"]:
            Infos.stack_key += key
        elif key == "i":
            Modes.change_mode(1)
            return
        elif key == "a":
            Modes.change_mode(1)
            if Infos.cursor_pos < len(Infos.input_string) + 1:
                Infos.cursor_pos += 1
            return
        elif key == "r":
            Modes.change_mode(2)
            return
        elif key == ":":
            Modes.change_mode(3)
            return

        if Infos.stack_key[-2:] == "dd":
            Infos.input_string = ""
            Infos.cursor_pos = 1
            Infos.stack_key = ""
            Draw.clear_input()
        elif Infos.stack_key[-1:] == " ":
            if Infos.stack_key[:-1].isdigit():
                Infos.cursor_pos += int(Infos.stack_key[:-1])
            else:
                Infos.cursor_pos += 1
            Infos.cursor_pos = min(Infos.cursor_pos, len(Infos.input_string) + 1)
            Infos.stack_key = ""
        elif Infos.stack_key[-1:] == "\x7f":
            if Infos.stack_key[:-1].isdigit():
                Infos.cursor_pos -= int(Infos.stack_key[:-1])
            else:
                Infos.cursor_pos -= 1
            Infos.cursor_pos = max(Infos.cursor_pos, 1)
            Infos.stack_key = ""
        Draw.actulise_input()
        Draw.draw_footer()

    def insert_mode(key: str):
        if key == "\x7f":
            Infos.input_string = Infos.input_string[:-1]
            Infos.cursor_pos = max(1, Infos.cursor_pos - 1)
            Functions.reset_tabulationIndex()
        elif key == "\r":
            if Infos.tabulationIndex == -1:
                sys.stdout.write(f"\033[2J\033[0;0H{Infos.input_string}\r\n")
                os.system(Infos.input_string)
                Draw.draw_footer()
                Config.write_history(Infos.input_string)
                Infos.history_index = 0
                Infos.history.append(Infos.input_string)
                Infos.input_string = ""
                Infos.cursor_pos = 1
            else:
                Infos.input_string = " ".join(Infos.input_string.split(" ")[:-1]) + " " + \
                                     Functions.auto_complete(Infos.input_string.split(" ")[-1], os.listdir("."))[
                                         Infos.tabulationIndex]
                Infos.cursor_pos = len(Infos.input_string) + 1
                Functions.reset_tabulationIndex()
        elif key == "\t":
            list_autocomplete = Functions.auto_complete(Infos.input_string.split(" ")[-1], os.listdir("."))
            Infos.tabulationIndex += 1
            for ind, i in enumerate(list_autocomplete):
                if ind == Infos.tabulationIndex:
                    sys.stdout.write(f"\033[33m\033[{ind + 2};1H{i}\033[0m")
                else:
                    sys.stdout.write(f"\033[{ind + 2};1H{i}")
        else:
            if Infos.input_string == "":
                Draw.clear_input()
            Infos.input_string = Infos.input_string[:Infos.cursor_pos - 1] + key + Infos.input_string[
                                                                                   Infos.cursor_pos - 1:]
            Infos.cursor_pos += 1
            Functions.reset_tabulationIndex()
        Draw.actulise_input()

    def all_mode(key: str):
        if key == "\x1b\x1b":
            Modes.change_mode(0)
            return

    @classmethod
    def get_mode_name(self):
        return self.allModes[self.currentMode].modName


def main():
    normalMode = Modes(0, "Normal", [])
    insertMode = Modes(1, "Insert", [])
    ReplaceMode = Modes(2, "Replace", [])
    CommandMode = Modes(3, "Command", [])
    clear()
    Draw.reload_all()
    while True:
        key = getKey(debug=True)
        sys.stdout.write("\033[0;0H")
        # print(get_key_bytes(True))
        if Modes.currentMode == 0:  # Normal Mode
            Modes.all_mode(key)
            Modes.normal_mode(key)
            Modes.normal_insert_mode(key)
        elif Modes.currentMode == 1:
            Modes.all_mode(key)
            Modes.insert_mode(key)
            Modes.normal_insert_mode(key)
        elif Modes.currentMode == 2:
            Modes.all_mode(key)
        elif Modes.currentMode == 3:
            Modes.all_mode(key)
        Draw.cursor_key()
        sys.stdout.flush()


if __name__ == "__main__":
    import sys

    if "--help" in sys.argv or "-h" in sys.argv:
        print("TODO")

    main()
