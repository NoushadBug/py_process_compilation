import os, tkinter as tk

class ConfigEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create input widgets
        self.label1 = tk.Label(self, text="Input 1")
        self.entry1 = tk.Entry(self)

        self.label2 = tk.Label(self, text="Input 2")
        self.entry2 = tk.Entry(self)

        self.button_save = tk.Button(self, text="Save", command=self.save_inputs)

        # Layout input widgets
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        self.button_save.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    
    def save_inputs(self):
        # Save input values to config.txt file
        input1_value = self.entry1.get()
        input2_value = self.entry2.get()

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
