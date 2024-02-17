import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Text Editor")
root.geometry("620x420")

text_widget = tk.Text(root)
text_widget.pack(fill="both", expand=True)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text_widget.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", "end"))

def cut():
    text_widget.event_generate("<<Cut>>")

def copy():
    text_widget.event_generate("<<Copy>>")

def paste():
    text_widget.event_generate("<<Paste>>")

def select_all():
    text_widget.tag_add("sel", "1.0", "end")

menu_bar = tk.Menu(root)

# create the file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# create the edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)


root.mainloop()