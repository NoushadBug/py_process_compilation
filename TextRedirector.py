class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        if "INFO::" in str:
            self.widget.insert("end", str, ("info",))
        elif "LOG::" in str:
            self.widget.insert("end", str, ("log",))
        elif "WARNING::" in str:
            self.widget.insert("end", str, ("warning",))
        elif "SUCCESS::" in str:
            self.widget.insert("end", str, ("success",))
        elif "ERROR::" in str:
            self.widget.insert("end", str, ("danger",))
        else:
            self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
        self.widget.update_idletasks()

    def flush(self):
        pass
