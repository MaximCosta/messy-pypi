import os
import sys
from main_terminalGetKey import getKey
def main():
    cmds = ["cd", "exit"]
    print("\033[2J\033[1;1H")
    while True:
        path = os.getcwd()
        cmd = input(f"{path = }:")
        if cmd.split(" ")[0] in cmds:
            execute(cmd)
        else:
            os.system(cmd)

def execute(cmd):
    if cmd[0:2] == "cd":
        os.chdir(cmd[3:])
    if cmd == "exit":
        exit()
if __name__ == "__main__":
    main()
