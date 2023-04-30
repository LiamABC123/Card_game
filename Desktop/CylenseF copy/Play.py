import time
import tkinter as tk
import os


class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()

        # window size
        self.root.geometry("800x600")

        # title and logo
        self.root.title("Cylense")
        self.root.iconphoto(True, tk.PhotoImage(file=os.path.abspath("logo.png")))

        # make window unresizable
        self.root.resizable(False, False)

        self.button_image_normal_5 = tk.PhotoImage(
            file=os.path.abspath("place_button.png")
        )
        self.button_image_hover_5 = tk.PhotoImage(
            file=os.path.abspath("place_button_hover.png")
        )

        self.button_image_normal_7 = tk.PhotoImage(
            file=os.path.abspath("draw_button.png")
        )
        self.button_image_hover_7 = tk.PhotoImage(file="draw_button_hover.png")
        # create photo objects for the button images
        self.button_image_normal_2 = tk.PhotoImage(file=os.path.abspath("button_2.png"))
        self.button_image_hover_2 = tk.PhotoImage(
            file=os.path.abspath("button_2_hover.png")
        )
        self.button_image_normal_5 = tk.PhotoImage(
            file=os.path.abspath("place_button.png")
        )
        self.button_image_hover_5 = tk.PhotoImage(
            file=os.path.abspath("place_button_hover.png")
        )
        self.button_image_normal_6 = tk.PhotoImage(
            file=os.path.abspath("gamble_button.png")
        )
        self.button_image_hover_6 = tk.PhotoImage(
            file=os.path.abspath("gamble_button_hover.png")
        )
        self.button_image_normal_8 = tk.PhotoImage(
            file=os.path.abspath("play_button.png")
        )
        self.button_image_hover_8 = tk.PhotoImage(
            file=os.path.abspath("play_button_hover.png")
        )
        self.button_image_normal_9 = tk.PhotoImage(
            file=os.path.abspath("exit_button.png")
        )
        self.button_image_hover_9 = tk.PhotoImage(
            file=os.path.abspath("exit_button_hover.png")
        )
        self.button_image_normal_4 = tk.PhotoImage(
            file=os.path.abspath("attack_button.png")
        )
        self.button_image_hover_4 = tk.PhotoImage(
            file=os.path.abspath("attack_button_hover.png")
        )
        # create photo objects for the button images
        self.button_image_normal = tk.PhotoImage(file=os.path.abspath("button_1.png"))
        self.button_image_hover = tk.PhotoImage(
            file=os.path.abspath("button_1_hover.png")
        )

        # create a button with the normal image and resize it
        self.button_4 = tk.Button(
            self.root,
            image=self.button_image_normal_4,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # create a button with the normal image and resize it
        self.button_9 = tk.Button(
            self.root,
            image=self.button_image_normal_9,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # create a button with the normal image and resize it
        self.button_8 = tk.Button(
            self.root,
            image=self.button_image_normal_8,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # create a button with the normal image
        self.button_2 = tk.Button(
            self.root,
            image=self.button_image_normal_2,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # create a button with the normal image and resize it
        self.button_7 = tk.Button(
            self.root,
            image=self.button_image_normal_7,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # create a button with the normal image and resize it
        self.button_5 = tk.Button(
            self.root,
            image=self.button_image_normal_5,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # create a button with the normal image
        self.button_3 = tk.Button(
            self.root,
            image=self.button_image_normal_3,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )
        # create a button with the normal image and resize it
        self.button_6 = tk.Button(
            self.root,
            image=self.button_image_normal_6,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )
        # create a button with the normal image
        self.button = tk.Button(
            self.root,
            image=self.button_image_normal,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # set background image
        self.bg_image = tk.PhotoImage(
            file="C:/Users/ex0ar/Desktop/CylenseF/background.png"
        )
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # calculate position of the window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = int((self.screen_width - 800) / 2)
        self.y = int((self.screen_height - 600) / 2)

        # set window position
        self.root.geometry("+{}+{}".format(x, y))

        # define button properties
        self.button_width = 142
        self.button_height = 62
        self.button_x = int(
            (800 - self.button_width) / 1.99
        )  # change this value to move the button left or right              higher = left
        self.button_y = int(
            (600 - self.button_height) / 2.14
        )  # change this value to move the button up or down                  higher = up

        # run the GUI
        self.root.mainloop()


gui = GUI()
