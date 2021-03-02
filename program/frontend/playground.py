from tkinter import filedialog
from tkinter import *
import os


def file_save():
    #name = filedialog.askopenfilename(initialdir = curr_directory,title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    dir_path = filedialog.askdirectory()
    file_name = f"{dir_path.split('/')[-1]}.ino"
    save_location = os.path.join(dir_path, file_name)    
    return dir_path


file_save()

