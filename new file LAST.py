import shutil
import tkinter
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import *

window = tk.Tk()
window.geometry("350x300+700+300")
window.title("NEW FILE")
window.resizable(False, False)
window['background'] = '#666666'


def new_button(x, y, bg, fg, cmd):
    def on_enter(e):
        my_button["background"] = bg
        my_button["foreground"] = fg

    def on_leave(e):
        my_button["background"] = fg
        my_button["foreground"] = bg

    my_button = Button(window,
                       width=20,
                       height=3,
                       text="NEW FILE",
                       fg=bg,
                       bg=fg,
                       activeforeground=fg,
                       activebackground=bg,
                       border=0,
                       font=("Calibri", 15, "bold"),
                       command=cmd,
                       )

    my_button.bind("<Enter>", on_enter)
    my_button.bind("<Leave>", on_leave)
    my_button.place(x=x, y=y)


def close_button(x, y, bg, fg, cmd):
    def on_enter(e):
        my_button["background"] = bg
        my_button["foreground"] = fg

    def on_leave(e):
        my_button["background"] = fg
        my_button["foreground"] = bg

    my_button = Button(window,
                       width=20,
                       height=3,
                       text="CLOSE",
                       fg=bg,
                       bg=fg,
                       activeforeground=fg,
                       activebackground=bg,
                       border=0,
                       font=("Calibri", 15, "bold"),
                       command=cmd,
                       )

    my_button.bind("<Enter>", on_enter)
    my_button.bind("<Leave>", on_leave)
    my_button.place(x=x, y=y)


def new_single_file():
    new_file = tkinter.filedialog.asksaveasfile(mode="w",
                                                defaultextension=".py",
                                                title="New File",
                                                filetypes=(("Python file", "*.py*"),))
    if new_file is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    new_file.close()
    # file name without .py
    new_file_path = new_file.name
    file_name = new_file.name.split('/').pop()
    directory = Path(new_file_path).parent
    new_file_path = file_name.rsplit(".", 1)[0]
    # rename
    old_name = "%s\%s" % (directory, file_name)
    new_file_path = new_file_path.lower().replace(".", "").replace(" ", "_")
    new_name = "%s\%s" % (directory, new_file_path + ".py")
    shutil.move(old_name, new_name)


def close():
    window.quit()


new_button(67, 45, "#00cc00", "#193300", new_single_file)
close_button(67, 157, "#cc0000", "#660000", close)

window.mainloop()
