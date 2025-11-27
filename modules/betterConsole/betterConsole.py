#----------------------------
# Better Console - V1.0.1
# © 2025 - do not redistribute
#----------------------------
# Recent edits: Better fullscreen mode, spacing better, code structure revamp and private varibles.
#----------------------------

from turtle import Screen, Turtle
from time import sleep
import re


import tkinter
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

__all__ = ["write", "ask", "hold", "customise", "reset", "byebye"]

_screen = Screen()
_root = _screen._root
_screen.setup(width=1.0, height=1.0)
_root.state('zoomed')

_canvas = _screen.getcanvas()
_canvas.config(highlightthickness=0.0, bd=1, bg="black")

_root.resizable(False, False)

_root.update()

# -----------------------------------------------------
# Customise these if you want
# -----------------------------------------------------

_screen.title("Better console - by tobble")
_screen.bgcolor("black")

width_Padding = 20
Hight_Padding = 40

COLOR_MAP = {
    "red": "#ff3333",
    "orange": "#ff9933",
    "yellow": "#ffff33",
    "green": "#33ff33",
    "blue": "#3399ff",
    "pink": "#FF9999",
    "purple": "#cc66ff",
    "white": "#ffffff",
    "grey": "#555555"
}

STYLE_MAP = {
    "bold": "bold",
    "italic": "italic",
    "underline": "underline",
    "normal": "normal"
}

# ----------------------------------------------------------
# DO NOT EDIT UNDER HERE UNLESS YOU KNOW WHAT YOUR DOING :)
# ----------------------------------------------------------

_screen.update()
_width = _screen.window_width()
_height = _screen.window_height()

_tXpos_default = -_width // 2 + width_Padding
_tYpos_default =  _height // 2 - Hight_Padding

_turtle = Turtle()
_turtle.hideturtle()
_turtle.penup()
_turtle.speed(9999)

_turtleYpos = _tYpos_default

def write(text, speed=0.01):
    global _turtleYpos
    _turtle.setpos(_tXpos_default, _turtleYpos)
    current_color = "white"
    current_style = "normal"
    _turtle.color(current_color)

    parts = re.split(r'(@\w+-)', text)

    for part in parts:
        match = re.match(r'@(\w+)-', part)
        if match:
            code = match.group(1).lower()
            if code in COLOR_MAP:
                current_color = COLOR_MAP[code]
                _turtle.color(current_color)
            elif code in STYLE_MAP:
                current_style = STYLE_MAP[code]
            continue

        for i in range(len(part)):
            ch = part[i]
            next_ch = part[i+1] if i + 1 < len(part) else ""
            _turtle.write(ch, font=('Arial', 16, current_style))

            if ch in [".", "!"]:
                sleep(0.5)
            else:
                sleep(speed)
                
            x, _ = _turtle.position()

            if ch in ["W", "M"]:
                spacing = 20
            elif ch.isupper() and next_ch != " ":
                spacing = 14 if ch not in ["I"] else 6
            elif ch in ["o"]:
                spacing = 12
            elif ch in ["r"]:
                spacing = 8
            elif ch in ["t", "f"]:
                spacing = 7
            elif ch in ["l", "i", "j", "'"]:
                spacing = 5
            elif ch in ["w", "m"]:
                spacing = 16
            elif ch in ["@"]:
                spacing = 20
            else:
                spacing = 11

            if current_style == "bold":
                spacing += 1
            
            _turtle.forward(spacing)

    _newline()

def ask(txt, speed=0.01):
    write(txt, speed)
    return askstring('input', 'enter input')

def hold():
    _screen.mainloop()

def customise(bgCol=None, title=None):
    _screen.title(title)
    _screen.bgcolor(bgCol)

def reset():
    global _turtleYpos
    _turtle.clear()
    _turtleYpos = _tYpos_default
    _turtle.setpos(_tXpos_default, _turtleYpos)

def byebye():
    _screen.bye()
    exit()
    
def _newline():
    global _turtleYpos
    _, y = _turtle.position()
    _turtleYpos = y - 30
    
    
def howto():
    print("----------------------------------------")
    print("Thank you for using better console by tobble © 2025.")
    print("----------------------------------------")
    print("To print text, use 'betterconsole.write(text, speed)'.")
    print("To take an input, use 'betterconsole.ask(text, speed)'.")
    print("----------------------------------------")
    print("To use colours and styles in text, use '@colour-' or '@style-'")
    print("----------------------------------------")
    print("Colours: @red-, @orange-, @yellow-, @green-, @blue-, @pink-, @purple-, @white-, @grey-.")
    print("styles: @bold-, @italic-, @underline-, @normal-.")
    print("----------------------------------------")
    print("More styles and colours can be added in the code under the 'COLOUR_MAP' and 'STYLE_MAP'.")
    print("----------------------------------------")

howto()
write("@grey-Better console by tobble. © 2025.", 0)
sleep(0.5)
reset()
