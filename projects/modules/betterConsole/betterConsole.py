#----------------------------
# Better Console - V1.0.1
# © 2025 - do not redistribute
#----------------------------
# Recent edits: more useful funcs, Better fullscreen mode, spacing better, code structure revamp and private varibles.
#----------------------------
#Edit these, if u want
#----------------------------

screenTitle = "Better console - by tobble"
screemColour = "black"

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

_defaultPause = 0.5

# ----------------------------------------------------------
# DO NOT EDIT UNDER HERE UNLESS YOU KNOW WHAT YOUR DOING :)
# ----------------------------------------------------------

from turtle import Turtle, Screen
import turtle
from time import sleep
import re

import sys

import tkinter
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

_TOMLLIB_WORKS = True

try:
    import tomllib
except ImportError:
    print("TOMLLIB NOT FOUND, FALLING BACK TO DEFAULT FONT. FONT CHANGES WILL NOT WORK.")
    _TOMLLIB_WORKS = False


import os

__all__ = ["write", "ask", "hold", "customise", "reset", "byebye", "wait"]

_screen = Screen()
_root = _screen._root
_screen.setup(width=1.0, height=1.0)
_root.state('zoomed')

_canvas = _screen.getcanvas()
_canvas.config(highlightthickness=0.0, bd=1, bg="black")

_root.resizable(False, False)

_root.update()

_screen.title(screenTitle)
_screen.bgcolor("black")
 
_screen.update()
_width = _screen.window_width()
_height = _screen.window_height()

_tXpos_default = -_width // 2 + width_Padding
_tYpos_default =  _height // 2 - Hight_Padding

_turtle = Turtle()
_turtle.hideturtle()
_turtle.penup()
_turtle.speed(0)

_turtleYpos = _tYpos_default

def load_font_rules():
    path = os.path.join(os.path.dirname(__file__), "font_rules.toml")
    with open(path, "rb") as f:
        return tomllib.load(f)

FONT_RULES = load_font_rules()
_currentFont = "Arial"

def write(text, speed=0.01):
    global _turtleYpos
    _turtle.setpos(_tXpos_default, _turtleYpos)
    current_color = "white"
    current_style = "normal"
    _turtle.color(current_color)

    parts = re.split(r'(@\w+-)', text)

    for part in parts:
        match = re.match(r'@([#\w]+)-', part)
        if match:
            code = match.group(1)

            if code.startswith("#") and re.fullmatch(r"#[0-9A-Fa-f]{6}", code):
                current_color = code
                _turtle.color(current_color)
                continue

            code_lower = code.lower()

            if code_lower in COLOR_MAP:
                current_color = COLOR_MAP[code_lower]
                _turtle.color(current_color)
                continue

            if code_lower in STYLE_MAP:
                current_style = STYLE_MAP[code_lower]
                continue

        for i in range(len(part)):
            ch = part[i]
            next_ch = part[i+1] if i + 1 < len(part) else ""
            _turtle.write(ch, font=(_currentFont, 16, current_style))
            
            if ch in [".", "!"]:
                sleep(0.5)
            else:
                sleep(speed)

            rules = FONT_RULES.get(_currentFont, {})
            default_spacing = rules.get("default", 11)
            caps_spacing = rules.get("caps")
            overrides = rules.get("override", {})

            if ch in overrides:
                spacing = overrides[ch]
            elif ch.isupper() and caps_spacing is not None:
                spacing = caps_spacing
            else:
                spacing = default_spacing

            if current_style == "bold":
                spacing += 1
                        
            _turtle.forward(spacing)

            if _turtle.xcor() > (_width // 2 - width_Padding):
                _newline()

    sleep(_defaultPause)
    _newline()

def ask(txt, speed=0.01):
    write(txt, speed)
    return askstring('input', 'enter input')

def hold():
    _screen.mainloop()

def customise(bgCol=None, title=None, pauseAfterWrite=None, font=None):
    global _currentFont, _defaultPause, FONT_RULES  # <-- add this
    if bgCol == None:
        pass
    else:
        _screen.bgcolor(bgCol)
    if title == None:
        pass
    else:
        _screen.title(title)
    if pauseAfterWrite == None:
        pass
    else:
        _defaultPause = pauseAfterWrite
    if font == None:
        pass
    else:
        FONT_RULES = load_font_rules()
        _currentFont = font

def reset():
    global _turtleYpos
    _turtle.clear()
    _turtleYpos = _tYpos_default
    _turtle.setpos(_tXpos_default, _turtleYpos)

def byebye():
    _screen.bye()
    exit()

def wait():
    write("@grey-Click enter to continue", 0)
    done = False
    def _pressed():
        nonlocal done
        done = True
    _screen.onkey(_pressed, "Return")
    _screen.listen()

    while not done:
        _screen.update()
        
def _newline():
    global _turtleYpos

    rules = FONT_RULES.get(_currentFont, {})
    newline_spacing = rules.get("newline", 30)

    _, y = _turtle.position()
    _turtleYpos = y - newline_spacing
    _turtle.setpos(_tXpos_default, _turtleYpos)

def _howto():
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

_howto()
write("@grey-Better console by tobble. © 2025.", 0)
sleep(0.5)
reset()
