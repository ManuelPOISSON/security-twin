import logging
import multiprocessing
import tkinter as tk
from tkinter import scrolledtext

from collector.collector import active_directory_collect, init_ad_context, logger


class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.after(0, self._append_text, msg)

    def _append_text(self, msg):
        self.text_widget.config(state='normal')
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.see(tk.END)
        self.text_widget.config(state='disabled')

class ApplicationGUI(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Inventory Agent")
        self.create()


    def create(self):
        self.entries = {}

        labels = {"ip_dc" : "IP Domain Controller", "domain" : "Domain Name", "user" : "Username", "password": "Password" }
        for (i, (assoc, label_text)) in enumerate(labels.items()):
            label = tk.Label(self, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
            show = ""
            if assoc == "password":
                show = "*"
            entry = tk.Entry(self, show=show, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[assoc] = entry

        self.log_level_var = tk.StringVar(value="INFO")

        log_frame = tk.LabelFrame(self, text="Logs Levels")
        log_frame.grid(row=0, column=2, rowspan=4, padx=10, pady=5, sticky='ns')

        for level in ["DEBUG", "INFO", "WARNING", "ERROR" ]:
            radio = tk.Radiobutton(log_frame, text=level, variable=self.log_level_var, value=level)
            radio.pack(anchor='w', padx=10, pady=2)

        launch_button = tk.Button(self, text="Launch", command=self.launch)
        launch_button.grid(row=4, column=0, columnspan=3, pady=10)

        self.log_text = scrolledtext.ScrolledText(self, width=80, height=10, state='disabled')
        self.log_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def parse_args(self):
        input = {}
        for key, value in self.entries.items():
            input[key] = value.get().strip()

        log_level = self.log_level_var.get()

        if log_level == "DEBUG":
            input["debug"] = True
        elif log_level == "INFO":
            input["verbose"] = False
        
        return input

    
    def launch(self):
        args = self.parse_args()
        context = init_ad_context(args)
        text_handler = TextHandler(self.log_text)

        text_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        text_handler.setLevel(logging.DEBUG)
        logger.addHandler(text_handler)
        if context is None:
            logger.error("Unable to initialize context from the arguments")
            return
        active_directory_collect(context)
        context.logger_manager.stop()
        

        



if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = ApplicationGUI()
    app.mainloop()