import tkinter as tk
from tkinter import messagebox

# Function to execute menu item 1
def open_prompt_creator():
    print("Opening prompt creator...")
    # Add your code here to open the prompt creator

# Function to execute menu item 2
def open_MJ():
    print("Opening MJ...")
    # Add your code here to open MJ

# Function to execute menu item 3
def open_MJ_profile():
    print("Opening MJ profile...")
    # Add your code here to open MJ profile

# Function to execute menu item 4
def run_extractor():
    print("Running Extractor...")
    # Add your code here to run the extractor

# Function to execute menu item 5
def run_gigapixel():
    print("Running Gigapixel...")
    # Add your code here to run Gigapixel

# Function to execute menu item 6
def process_in_lightroom():
    print("Processing in Lightroom...")
    # Add your code here to process in Lightroom

# Function to execute menu item 7
def property_releases():
    print("Running Property Releases...")
    # Add your code here to run the property releases

# Function to execute menu item 8
def run_WP2JPG():
    print("Running WP2JPG...")
    # Add your code here to run WP2JPG

# Function to execute menu item 9
def open_folders():
    print("Opening folders...")
    # Add your code here to open folders

# Function to execute menu item 10
def delete_folder_contents():
    print("Deleting folder contents...")
    # Add your code here to delete folder contents


# Create the main window
window = tk.Tk()

# Set the window title and size
window.title("Process Flow Menu")
window.geometry("500x400")
window.configure(bg="#F5F5F5")
window.attributes('-alpha', 0.9)
window.attributes("-topmost", True)

# Set the radius of the rounded borders
button_radius = 10

# Create the menu items as buttons
button1 = tk.Button(window, text="Open Prompt Creator", command=open_prompt_creator, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button2 = tk.Button(window, text="Open MJ", command=open_MJ, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button3 = tk.Button(window, text="Open MJ Profile", command=open_MJ_profile, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button4 = tk.Button(window, text="Run Extractor", command=run_extractor, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button5 = tk.Button(window, text="Run Gigapixel", command=run_gigapixel, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button6 = tk.Button(window, text="Process in Lightroom", command=process_in_lightroom, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button7 = tk.Button(window, text="Property Releases", command=property_releases, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button8 = tk.Button(window, text="Run WP2JPG", command=run_WP2JPG, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button9 = tk.Button(window, text="Open Folders", command=open_folders, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")
button10 = tk.Button(window, text="Delete Folder Contents", command=delete_folder_contents, width=20, height=2, bd=0, bg="#E0E0E0", relief="solid", borderwidth=1, highlightthickness=0, padx=10, pady=10, font=("Helvetica", 12), border=0, highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", activebackground="#BDBDBD", activeforeground="#FFFFFF")

# Pack the buttons onto the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()

# Run the window loop
window.mainloop()
