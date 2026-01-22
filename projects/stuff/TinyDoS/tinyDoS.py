#----------------------------
# TinyDos
# © 2026 - do not redistribute
#----------------------------

import tkinter as tk
import os

# --------------------
# state
# --------------------

current_dir = "root"
prompt_index = "1.0"

USAGE = {
    "run": "run <program>",
    "dir": "dir in <path> | dir create <name>",
}

# --------------------
# tkinter setup
# --------------------

root = tk.Tk()
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.overrideredirect(True)

FONT = ("Consolas", 12)

text = tk.Text(
    root,
    bg="black",
    fg="white",
    insertbackground="white",
    font=FONT,
    wrap="word",
    bd=0,
    highlightthickness=0,
    selectbackground="white",
    selectforeground="black"
)
text.pack(fill="both", expand=True)
text.focus()

# --------------------
# helpers
# --------------------

def write(s=""):
    global prompt_index
    text.insert("end", s + "\n")
    text.see("end")
    prompt_index = text.index("end-1c")

def clear():
    text.delete("1.0", "end")

def show_prompt():
    global prompt_index
    text.insert("end", f"{current_dir}> ")
    prompt_index = text.index("end-1c")
    text.mark_set("insert", "end")

# --------------------
# command system
# --------------------

def commands(text_input):
    if not text_input.strip():
        return

    parts = text_input.split()
    cmd_name = parts[0]
    args = parts[1:]

    try:
        globals()[f"cmd_{cmd_name}"](*args)
    except KeyError:
        write(f"Command error: The command '{cmd_name}' was unrecognised.")
    except TypeError:
        write(f"Command error: Invalid parameters for '{cmd_name}'.")
        if cmd_name in USAGE:
            write(f"Usage: {USAGE[cmd_name]}")

#---------------------
# file system helpers
#---------------------
def createDir(directory):
    global current_dir
    path = f"./{current_dir}/{directory}"
    write(f"creating at {path}")
    os.mkdir(path)

def createRoot():
    os.mkdir("./root")
# --------------------
# commands
# --------------------

def cmd_help():
    write("commands:")
    write("├ exit - exits tiny OS")
    write("├ run <program> - runs a program")
    write("├ dir in <path> | dir create <name> - make this directory")
    write("├ clr - clear screen")

def cmd_run(program):
    write(f"Running program: {program}")

def cmd_dir(action, param):
    global current_dir
    if action == "in":
        if os.path.isdir(param):
            current_dir = param
        else:
            write("Error: dir doesnt exist.")
    elif action == "create":
        createDir(param)

def cmd_clr():
    clear()

def cmd_exit():
    root.destroy()

def cmd_col(col):
    try:
        text.configure(
            fg=col,
            insertbackground=col
        )
    except tk.TclError:
        write(f"Invalid colour: {col}")

# --------------------
# key handling
# --------------------

def on_key(event):
    # prevent editing old text
    if text.compare("insert", "<", prompt_index):
        text.mark_set("insert", "end")

    # enter pressed
    if event.keysym == "Return":
        cmd = text.get(prompt_index, "end-1c")
        write("")
        commands(cmd)
        show_prompt()
        return "break"

    # block backspace before prompt
    if event.keysym == "BackSpace":
        if text.compare("insert", "<=", prompt_index):
            return "break"

text.bind("<Key>", on_key)

# --------------------
# banner
# --------------------

write(r" _______              ___       ____ ")
write(r"/_  __(_)__  __ __   / _ \___  / __/")
write(r" / / / / _ \/ // /  / // / _ \_\ \  ")
write(r"/_/ /_/_//_/\_  /  /____/\___/___/  ")
write(r"           /___/                    ")
write("Tiny DoS by Tobble - Copyright 2025")
write("Type 'help' for help")
write("")
show_prompt()

try:
    createRoot()
except:
    pass

# --------------------
# start
# --------------------

root.mainloop()
