#!/usr/bin/python3
# -----------------------------------------------------------------
# this is simple program for generating random,
# number, using tkinter.
#
#
#
# Author:N84.
#
# Create Date:Sun Feb 20 15:29:35 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from random import randint
import tkinter
from os import system
from os import name as os_name


# default width and height of the window.
WIN_WIDTH = 550
WIN_HEIGHT = 200
WIN_BG = "gray66"
WIN_FONT = "ubuntu"


def clear():
    """function to wipe the terminal."""
    if os_name == "posix":
        # for *nix machines.
        system("clear")

    elif os_name == "windows":
        system("cls")

    else:
        # for all other os in the world.
        # system("your-command")
        pass


def start_app(root: tkinter.Tk):
    """"""
    root.mainloop()

    return None


def generate_rand_num(string_var: tkinter.StringVar):
    """generate random number and appending it to the StringVar object,
    that we pass."""

    random_number = randint(0, 1000)

    temp_string = f"OUTPUT: [{str(random_number).zfill(2)}]"

    string_var.set(temp_string)

    return None


def main_window():
    """"""

    root = tkinter.Tk()

    root.title("Random Number")

    root.resizable(False, False)

    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    root.configure(bg=WIN_BG)

    # create special var to store the random,
    # number value in to it.
    random_number = tkinter.StringVar()

    # set an init value for random number.
    random_number.set('OUTPUT: [-]')

    btn_properties = {
        "bd": 0,
        "bg": "gray80",
        "highlightthickness": 0,
        "activebackground": "gray85",
        "font": (WIN_FONT, 24, "bold")
    }
    label_properties = {
        "bd": 0,
        "bg": WIN_BG,
        "fg": "gray33",
        "font": (WIN_FONT, 24, "bold")
    }

    generate_random_number_btn = tkinter.Button(
        root, text="Generate", command=lambda: generate_rand_num(random_number), **btn_properties)

    generate_random_number_btn.pack()

    output_label = tkinter.Label(
        root, textvariable=random_number, **label_properties)

    # output_label.place(x=165, y=140)
    output_label.pack()

    start_app(root)

    return None


def main():
    main_window()


if __name__ == "__main__":
    main()
