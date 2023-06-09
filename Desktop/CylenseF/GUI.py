import random
import time
import tkinter as tk

def create_gui():
    root = tk.Tk()

    # window size
    root.geometry("800x600")

    # title and logo
    root.title("Cylense")
    root.iconphoto(True, tk.PhotoImage(file="logo.png"))

    # make window unresizable
    root.resizable(False, False)

    # set background image
    bg_image = tk.PhotoImage(file="C:/Users/ex0ar/Desktop/CylenseF/background.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # calculate position of the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - 800) / 2)
    y = int((screen_height - 600) / 2)

    # set window position
    root.geometry("+{}+{}".format(x, y))

    # define button properties
    button_width = 142
    button_height = 62
    button_x = int((800 - button_width) / 1.99) # change this value to move the button left or right              higher = left
    button_y = int((600 - button_height) / 2.14) # change this value to move the button up or down                  higher = up

    # create photo objects for the button images
    button_image_normal = tk.PhotoImage(file="button_1.png")
    button_image_hover = tk.PhotoImage(file="button_1_hover.png")

    # create a button with the normal image
    button = tk.Button(root, image=button_image_normal, width=button_width, height=button_height, bd=0, relief="sunken", highlightthickness=0, activebackground="white")

    # define function to switch button image on mouse hover
    def switch_button_image(event):
        button.config(image=button_image_hover)

    def switch_button_image_back(event):
        button.config(image=button_image_normal)


    def clear_gui_1(event):
        # destroy all buttons
        button.destroy()
        button_2.destroy()
        button_3.destroy()

        # change background image
        bg_image = tk.PhotoImage(file="background_ingame.png")
        bg_label.config(image=bg_image)
        bg_label.image = bg_image
        # create photo objects for the button images
        button_image_normal_4 = tk.PhotoImage(file="attack_button.png")
        button_image_hover_4 = tk.PhotoImage(file="attack_button_hover.png")

        # create a button with the normal image and resize it
        button_4 = tk.Button(root, image=button_image_normal_4, width=100, height=103, bd=0, relief="sunken", highlightthickness=0, activebackground="white")

        # reposition the button and place it on the window
        button_4.place(x=47, y=474, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_4(event):
            button_4.config(image=button_image_hover_4)

        def switch_button_image_back_4(event):
            button_4.config(image=button_image_normal_4)

        # bind the button hover events to switch_button_image function
        button_4.bind("<Enter>", switch_button_image_4)
        button_4.bind("<Leave>", switch_button_image_back_4)

        # define function to exit the GUI
        def exit_gui(event):
            time.sleep(1)
            root.destroy()
        
        # bind the button click event to exit_gui function
        button_4.bind("<Button-1>", exit_gui) ##########################################################################

    def clear_gui_2(event):
        # destroy all buttons
        button.destroy()
        button_2.destroy()
        button_3.destroy()
        bg_image = tk.PhotoImage(file="background_info.png")
        bg_label.config(image=bg_image)
        bg_label.image = bg_image
        text_frame = tk.Frame(root, bg="#343541", highlightthickness=0, bd=0)
        text_frame.place(relx=0.5, rely=0.384, relwidth=0.85, relheight=0.57, anchor="center")
        text_widget = tk.Text(text_frame, font=("Lemon Milk Pro Regular", 17), bg="#343541", fg="white", wrap="word", bd=0, highlightthickness=0)
        text_widget.insert("end", "Welcome to Cylense! In this game, you'll be facing off against a bot with your own deck of 25 cards. At the start of each game, you and your opponent will draw 5 cards from your deck. During your turn, you'll have the option to place a monster card onto your field, attack with a monster on your field, gamble for a chance at a positive or negative outcome, or draw a new card. Be careful not to let your hand get too full, as you can only have a maximum of 7 cards at a time. When attacking, the difference between your monster's ATTACK stat and the opposing monster's DEFENSE stat determines how much damage you or your opponent will take. Each player starts with 10000 lifepoints, and the goal is to whittle your opponent's lifepoints down to zero before they do the same to you. Good luck, and have fun playing!")
        text_widget.config(state="disabled")
        text_widget.pack(fill="both", expand=True)

    # bind the button hover events to switch_button_image function
    button.bind("<Enter>", switch_button_image)
    button.bind("<Leave>", switch_button_image_back)
    
    # bind the button click event to clear_gui function
    button.bind("<Button-1>", clear_gui_1)
    
    # place the button on the window
    button.place(x=button_x, y=button_y, anchor="nw")
















    # create photo objects for the button images
    button_image_normal_2 = tk.PhotoImage(file="button_2.png")
    button_image_hover_2 = tk.PhotoImage(file="button_2_hover.png")

    # create a button with the normal image
    button_2 = tk.Button(root, image=button_image_normal_2, width=button_width, height=button_height, bd=0, relief="sunken", highlightthickness=0, activebackground="white")

    # define function to switch button image on mouse hover
    def switch_button_image_2(event):
        button_2.config(image=button_image_hover_2)

    def switch_button_image_back_2(event):
        button_2.config(image=button_image_normal_2)

    # bind the button hover events to switch_button_image function
    button_2.bind("<Enter>", switch_button_image_2)
    button_2.bind("<Leave>", switch_button_image_back_2)
    button_2.bind("<Button-1>", clear_gui_2)

    # place the button on the window below the first button
    button_2.place(x=button_x, y=button_y+button_height+10, anchor="nw")











    # create photo objects for the button images
    button_image_normal_3 = tk.PhotoImage(file="button_3.png")
    button_image_hover_3 = tk.PhotoImage(file="button_3_hover.png")

    # create a button with the normal image
    button_3 = tk.Button(root, image=button_image_normal_3, width=button_width, height=button_height, bd=0, relief="sunken", highlightthickness=0, activebackground="white")

    # define function to switch button image on mouse hover
    def switch_button_image_3(event):
        button_3.config(image=button_image_hover_3)

    def switch_button_image_back_3(event):
        button_3.config(image=button_image_normal_3)

    # bind the button hover events to switch_button_image function
    button_3.bind("<Enter>", switch_button_image_3)
    button_3.bind("<Leave>", switch_button_image_back_3)

    # place the button on the window below the second button
    button_3.place(x=button_x, y=button_y+(2*button_height)+20, anchor="nw")

    # define function to exit the GUI
    def exit_gui(event):
        time.sleep(1)
        root.destroy()
    
    # bind the button click event to exit_gui function
    button_3.bind("<Button-1>", exit_gui)

    # run the GUI
    root.mainloop()

create_gui()
