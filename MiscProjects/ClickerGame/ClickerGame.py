#---------------
# Imports
#---------------

import tkinter as tk

#-----------------------
# Variabes / Game stats
#-----------------------

clicks = 0
click_power = 1
clicks_per_sec = 0

# Upgrades:
upgrades = [
    {
        "name": "Stronger Click",
        "utype": "per_click",
        "cost": 10,
        "effect": 1,
        "level": 0,
        "cost_mult": 1.5
    },
    {
        "name": "Auto Clicker",
        "utype": "per_sec",
        "cost": 50,
        "effect": 1,
        "level": 0,
        "cost_mult": 1.5
    }
]

#---------------
# Game Functions
#---------------


# This will let a few other functions update
# the state of the game easier.
def update_display():
    clicks_count.config(text=f"Clicks: {clicks}")

    upgrade1_button.config(
        text=f"{upgrades[0]['name']}, Cost: {upgrades[0]['cost']} Clicks"
    )

    upgrade2_button.config(
        text=f"{upgrades[1]['name']}, Cost: {upgrades[1]['cost']} Clicks"
    )


# Handles cases wher spending "money" is involved.
def buying(upgrade):
    global clicks, click_power, clicks_per_sec

    if clicks >= upgrade["cost"]:

            if upgrade["utype"] == "per_click":
                click_power += upgrade["effect"]

            elif upgrade["utype"] == "per_sec":
                clicks_per_sec += upgrade["effect"]

            clicks -= upgrade["cost"]

            upgrade["cost"] = round(
                upgrade["cost"] * upgrade["cost_mult"])

            upgrade["level"] += 1
            
            update_display()

    else:
        print("Not enough clicks.")


# This function adds to the total clicks
# every time the button is pressed.
def clicked_button():
    global clicks

    clicks += click_power
    update_display()

# Adds clicks per sec, and updates display.
def passive_income():
    global clicks

    clicks += clicks_per_sec
    update_display()

    window.after(1000, passive_income)


# This was suppost to be a genaric open menu, but
# because it specifies where the menu will open to 
# it has become an open just for the menu.
def open_menu_panel(panel):
    panel.place(
        relx=0.15,
        rely=0.1,
        relwidth=0.7, 
        relheight=0.8
    )
    panel.lift()


# Same as the last open menu, spicific location makes
# it non-genaric.
def open_upgrade_panel(panel):
    shrink_game()
    upgrades_button.grid_remove()

    panel.place(
        relx= 0.6, 
        rely=0, 
        relwidth=0.4, 
        relheight=1
    )


# CLoses the menu panel.
def close_m_panel(panel):
    panel.place_forget()


# Closes the upgrade menu
def close_up_panel():
    upgrade_frame.place_forget()
    upgrades_button.grid()

    game_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
    )


# This should set the size of the main window
# only when the upgrades window is open, making it
# apear as if the upgrade screen shrinks the main window.
def shrink_game():
    game_frame.place(
        relx=0,
        rely=0,
        relwidth=0.6,
        relheight=1
    )
#--------------
# Main Window
#--------------

window = tk.Tk()

window.title("My Clicker Game")
window.geometry("500x500")

#--------
# Frames
#--------

game_frame = tk.Frame(
    window, 
    bg="tan"
)
game_frame.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
)

upgrade_frame = tk.Frame(
    window,
    bg="lightblue"
)

menu_frame = tk.Frame(
    game_frame, 
    bg="lightgray"
)

#----------
# Widgets
#----------

# Game Controls
clicks_count = tk.Label(
    game_frame, 
    text=f"Clicks: {clicks}", 
    font=("arial", 23), 
    bg="tan"
)
clicks_count.grid(
    row=1, 
    column=1,
    sticky="nsew"
)

click_button = tk.Button(
    game_frame, 
    text="CLICK!", 
    command=clicked_button, 
    font=("arial", 30)
)
click_button.grid(
    row=2, 
    column=1
)

# Menu Options
menu_button = tk.Button(
    game_frame, 
    text="MENU", 
    command=lambda: open_menu_panel(menu_frame)
)
menu_button.grid(
    row=0,
    column=0,
    sticky="nw",
    padx=10,
    pady=10
)

menu_label = tk.Label(
    menu_frame, 
    text="Menu",
    font=("arial", 16), 
    bg="lightgray"
)
menu_label.grid(
    row=0, 
    column=1
)

settings_button = tk.Button(
    menu_frame, 
    text="Settings", 
    bg="lightgray"
)
settings_button.grid(
    row=1, 
    column=1,
    sticky="ew",
    padx=20,
    pady=5
)

stats_button = tk.Button(
    menu_frame, 
    text="Stats", 
    bg="lightgray"
)
stats_button.grid(
    row=2, 
    column=1,
    sticky="ew",
    padx=20,
    pady=5
)

save_button = tk.Button(
    menu_frame, 
    text="Save", 
    bg="lightgray"
)
save_button.grid(
    row=3, 
    column=1,
    sticky="ew",
    padx=20,
    pady=5
)

saveq_button = tk.Button(
    menu_frame, 
    text="Save and Quit", 
    bg="red"
)
saveq_button.grid(
    row=4, 
    column=1,
    sticky="ew",
    padx=20,
    pady=5
)

close_m_button = tk.Button(
    menu_frame, 
    text="Close", 
    command=lambda: close_m_panel(menu_frame), 
    bg="green"
)
close_m_button.grid(
    row=5, 
    column=1,
    sticky="ew",
    padx=20,
    pady=5
)

# Upgrades Menu
upgrades_button = tk.Button(
    game_frame, 
    text="Upgrades", 
    command=lambda: open_upgrade_panel(upgrade_frame)
)
upgrades_button.grid(
    row=0,
    column=2,
    sticky="new"
)

upgrade_header = tk.Frame(
    upgrade_frame,
    bg="lightblue"
)
upgrade_header.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew"
)
close_up_button = tk.Button(
    upgrade_header, 
    text="X", 
    bg="red", 
    command=close_up_panel
)
close_up_button.grid(
    row=0,
    column=1,
    sticky="ne",
    padx=5,
    pady=5
)

upgrade_label = tk.Label(
    upgrade_header,
    text="Upgrades",
    font=("arial", 16),
    bg="lightblue"
)
upgrade_label.grid(
    row=0,
    column=0,
    sticky="w",
    padx=10
)

upgrade1_button = tk.Button(
    upgrade_frame,
    text=f"{upgrades[0]['name']}, Cost: {upgrades[0]['cost']} Clicks",
    command=lambda: buying(upgrades[0])
)
upgrade1_button.grid(
    row=1,
    column=1
)

upgrade2_button = tk.Button(
    upgrade_frame,
    text=f"{upgrades[1]['name']}, Cost: {upgrades[1]['cost']} Clicks",
    command=lambda: buying(upgrades[1])
)
upgrade2_button.grid(
    row=2,
    column=1
)

#--------------------
# Alignment Widgets
#--------------------

# Game_frame alignment.
game_frame.columnconfigure(0, weight=1)
game_frame.columnconfigure(1, weight=1)
game_frame.columnconfigure(2, weight=1)

game_frame.rowconfigure(0, weight=1)
game_frame.rowconfigure(1, weight=1)
game_frame.rowconfigure(2, weight=1)

# Menu_framr alignment
menu_frame.columnconfigure(0, weight=1)
menu_frame.columnconfigure(1, weight=1)
menu_frame.columnconfigure(2, weight=1)

# Upgrade_header alignment
upgrade_header.columnconfigure(0, weight=1)
upgrade_header.columnconfigure(1, weight=0)

#------------
# Game Start
#------------

window.after(1000, passive_income)
window.mainloop()