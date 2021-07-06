import main_terminalkey


class Collector:
    menu = False

    @classmethod
    def show_menu(cls):
        cls.menu = not cls.menu


key_functions = {
    "\x1b": Collector.show_menu,

}

if __name__ == "__main__":
    main_terminalkey.main()
