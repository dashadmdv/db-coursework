from cli.cli import CLI
import tkinter as tk

from gui.gui import GUI


def main():
    # cli = CLI()
    # cli.run()
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()