import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import os
from helpers import *


class LoadingPages:
    def __init__(self, master=None):

        self.root = master

        self.bg_frame = Image.open('assets\\backgroud.jpg')
        self.photo = ImageTk.PhotoImage(self.bg_frame) 
        self.bg_panel = tk.Label(self.root, image = self.photo)
        self.bg_panel.image = self.photo
        self.bg_panel.pack(fill = 'both', expand = 'yes')

        # Window Size and Positioning
        window_size_and_positioning_530_x_430(self.root)
        self.root.overrideredirect(True)    

        self.progress = ttk.Style()
        self.progress.theme_use('clam')
        self.progress.configure("red.Horizontal.TProgressbar", background = "#108cff")

        self.progress_bar  = ttk.Progressbar(self.root, orient='horizontal', length = 400, mode = 'determinate', style = "red.Horizontal.TProgressbar")
        self.progress_bar.place(x = 60, y = 400)           

        i = 0

        def load():
            nonlocal i 
            if i <= 100:
                self.progress_bar['value'] = i
                i += 1
                self.root.after(50, load)
            else:
                self.root.destroy()
                os.system("python ILoginForm.py")
                
        load()