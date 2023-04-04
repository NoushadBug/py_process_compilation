import tkinter as tk, tkinter.messagebox as msgbox
import getpass, sys, os, ttkbootstrap as ttk
from ttkbootstrap.constants import *
from data import *
from datetime import datetime
from functions import *
from config_editor import ConfigEditor

full_name = getpass.getuser()

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


def show_output(cmd):

    # Clear the old frame if it exists
    main_frame.destroy()

    # Create a new frame
    output_frame = ttk.Frame(root, padding=10)
    output_frame.pack(fill=tk.BOTH, expand=True)

    # Add a "Home" button to go back to the main screen
    home_button = ttk.Button(output_frame, text="Home", command=lambda: switch_window(create_main_frame()))
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
    # Destroy the current frame
    root.output_frame.destroy()
    # Call the given frame function to create the new frame
    frame_function()

def create_config_editor_frame():
    # Clear the old frame if it exists
    main_frame.destroy()

    # Create a new frame
    config_frame = ttk.Frame(root, padding=10)
    config_frame.pack(fill=tk.BOTH, expand=True)

    # Add a "Home" button to go back to the main screen
    home_button = ttk.Button(config_frame, text="Home", command=lambda: switch_window(create_main_frame()))
    home_button.pack(side=tk.BOTTOM, pady=10)

    # Save the new frame to the root object
    root.output_frame = config_frame

    # Read values from config.txt if available
    inputs = {}
    try:
        with open("config.txt", "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                inputs[key] = value
    except FileNotFoundError:
        pass

    # Create input widgets
    input_widgets = []
    for key in inputs.keys():
        label = tk.Label(config_frame, text=key)
        entry = tk.Entry(config_frame)
        entry.insert(0, inputs[key])
        input_widgets.append((label, entry))

    # Create "Add" button to add new input fields
    def add_input():
        label = tk.Label(config_frame, text="Input " + str(len(input_widgets) + 1))
        entry = tk.Entry(config_frame)
        input_widgets.append((label, entry))
        label.pack(padx=5, pady=5, anchor=tk.W)
        entry.pack(padx=5, pady=5)

    add_button = tk.Button(config_frame, text="Add", command=add_input)
    add_button.pack(padx=5, pady=5)

    # Create "Save" button to save inputs to file
    def save_inputs():
        with open("config.txt", "w") as f:
            for label, entry in input_widgets:
                key = label.cget("text")
                value = entry.get()
                f.write(key + "=" + value + "\n")

    save_button = tk.Button(config_frame, text="Save", command=save_inputs)
    save_button.pack(padx=5, pady=5)

    # Layout input widgets
    for label, entry in input_widgets:
        label.pack(padx=5, pady=5, anchor=tk.W)
        entry.pack(padx=5, pady=5)

    # Focus on the first input field
    if input_widgets:
        input_widgets[0][1].focus_set()



def save_inputs(entry1, entry2):
    # Save input values to config.txt file
    input1_value = entry1.get()
    input2_value = entry2.get()

    if not os.path.exists("config.txt"):
        with open("config.txt", "w") as f:
            f.write(f"input1=\n")
            f.write(f"input2=\n")

    with open("config.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.startswith("input1="):
                f.write(f"input1={input1_value}\n")
            elif line.startswith("input2="):
                f.write(f"input2={input2_value}\n")
            else:
                f.write(line)
        f.truncate()


# Create main frame
create_main_frame()


# Create menu bar
menu_bar = ttk.Menu(root)
root.config(menu=menu_bar)

# Create config editor menu
config_editor_menu = ttk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Config", menu=config_editor_menu)
config_editor_menu.add_command(label="Edit Config", command=create_config_editor_frame)

# Center window on screen
root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w/2 - size[0]/2
y = h/2 - size[1]/2
root.geometry("%dx%d+%d+%d" % (size + (x, y)))

root.mainloop()
