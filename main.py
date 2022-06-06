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
WIN_HEIGHT = 600
WIN_BG = "gray66"


def clear():
    """function to wipe the terminal."""
    if os_name == "posix":
        # for *nix machines.
        system("clear")
    else:
        # for windows machines.
        system("cls")


def start_app(root: tkinter.Tk):
    root.mainloop()


def generate_rand_num(string_var: tkinter.StringVar):

    random_number = randint(0, 1000)

    temp_string = f"OUTPUT: [{str(random_number).zfill(2)}]"

    string_var.set(temp_string)


def main_window():

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

    generate_random_number_btn = tkinter.Button(
        root, text="Generate", bd=0, bg="gray80", highlightthickness=0, activebackground="gray85", font=("Calbri", 24, "bold"), command=lambda: generate_rand_num(random_number))
    # generate_random_number_btn.place(x=185, y=40)
    generate_random_number_btn.pack()

    output_label = tkinter.Label(
        root, textvariable=random_number, bg=WIN_BG, fg="gray33", font=("Calbri", 24, "bold"))

    # output_label.place(x=165, y=140)
    output_label.pack()

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()