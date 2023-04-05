import tkinter as tk, tkinter.messagebox as msgbox
from tkinter import scrolledtext
import getpass, sys, os, ttkbootstrap as ttk
from ttkbootstrap.constants import *
from data import *
from datetime import datetime
from functions import *
from config_editor import ConfigEditor

full_name = getpass.getuser()
isConfig = False
root = ttk.Window()
root.title("Process Compilation Tool")


def create_main_frame():
    global main_frame

    # Create main frame
    main_frame = ttk.Frame(root, padding=1)
    main_frame.pack(fill=tk.BOTH, expand=True)


    # Add menu items to input menu


    # Add the title
    title_label = tk.Label(main_frame, text=f"Hello {full_name}!", font=("TkDefaultFont", 18))
    title_label.pack(side=tk.TOP, pady=5)


    # Add the small heading for time and day
    now = datetime.now()
    time_label = tk.Label(main_frame, text=now.strftime("%A, %d %B %Y"), font=("TkDefaultFont", 12))
    time_label.pack(side=tk.TOP)

    separator = ttk.Separator(main_frame, orient=tk.HORIZONTAL)
    separator.pack(side=tk.TOP, fill=tk.X, pady=5)

    # Create button frame
    button_frame = ttk.Labelframe(main_frame, text="Automation Actions")
    button_frame.pack(side=tk.TOP, pady=10, fill=tk.X)

    # Create buttons using a loop
    for i, (button_text, button_opts) in enumerate(button_data.items()):
        button = ttk.Button(button_frame, text=button_text, **button_opts, width=20)
        button.configure(command=lambda cmd=button_opts["command"]: show_output(cmd))
        button.grid(row=i//2, column=i%2, padx=5, pady=5)
    
    return main_frame

def show_output(cmd):

    # Clear the old frame if it exists
    main_frame.destroy()

    # Create a new frame
    output_frame = ttk.Frame(root, padding=10)
    output_frame.pack(fill=tk.BOTH, expand=True)

    # Add a "Home" button to go back to the main screen
    home_button = ttk.Button(output_frame, text="Home", command=lambda: switch_window(create_main_frame))
    home_button.pack(side=tk.BOTTOM, pady=10)
    home_button.configure(state=tk.DISABLED)

    # Save the new frame to the root object
    root.output_frame = output_frame

    # Create a text widget and scrollbar
    output_text = tk.Text(output_frame)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=output_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    output_text.tag_configure("log", foreground="black")
    output_text.tag_configure("info", foreground="blue")
    output_text.tag_configure("warning", foreground="orange")
    output_text.tag_configure("success", foreground="green")
    output_text.tag_configure("danger", foreground="red")
    output_text.configure(yscrollcommand=scrollbar.set)

    # Redirect stdout to the text widgetx
    sys.stdout = TextRedirector(output_text, "stdout")

    # Call the command function and print the output
    cmd()
    # Enable home button after the command completes
    home_button.configure(state=tk.NORMAL)

def switch_window(frame_function):
    print(frame_function)
    # Destroy the current frame
    root.output_frame.destroy()
    # Call the given frame function to create the new frame
    frame_function()


def save_inputs(config_text):
    with open("config.txt", "w") as f:
        f.write(config_text.get("1.0", tk.END))

def create_config_editor_frame():
    # Clear the old frame if it exists
    main_frame.destroy()

    # Create a new frame
    config_frame = ttk.Frame(root, padding=10)
    config_frame.pack(fill=tk.BOTH, expand=True)

    # Create a frame for the buttons
    button_frame = ttk.Frame(config_frame, height=1)
    button_frame.pack(side=tk.BOTTOM, pady=10, padx=5)

    # Add a "Home" button to go back to the main screen
    home_button = ttk.Button(button_frame, text="Home", width=10, command=lambda: switch_window(create_main_frame))
    home_button.pack(side=tk.LEFT, padx=5)

    # Create "Save" button to save inputs to file
    save_button = tk.Button(button_frame, text="Save", width=10, command=lambda: save_inputs(config_text))
    save_button.pack(side=tk.RIGHT, padx=5)

    # Create a scrolledtext widget to display the contents of config.txt
    config_text = scrolledtext.ScrolledText(config_frame, width=60, height=20)
    config_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    # Add the contents of config.txt to the scrolledtext widget
    with open("config.txt", "r") as f:
        config_text.insert(tk.END, f.read())

    # Focus on the scrolledtext widget
    config_text.focus_set()

    # Save the new frame to the root object
    root.output_frame = config_frame
    return config_frame

# Create main frame
create_main_frame()


# Create menu bar
menu_bar = ttk.Menu(root)
root.config(menu=menu_bar)

# Create config editor menu
config_editor_menu = ttk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Config", menu=config_editor_menu)
config_editor_menu.add_command(label="Edit Config", command=lambda: create_config_editor_frame())

# Center window on screen
root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w/2 - size[0]/2
y = h/2 - size[1]/2
root.geometry("%dx%d+%d+%d" % (size + (x, y)))

root.mainloop()
