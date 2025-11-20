#----------------------------
#Better Console - V1.0.1
#© 2025 - do not redistribute
#----------------------------


from turtle import Screen, Turtle
from time import sleep
import re

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.title("Better console")
screen._root.state('zoomed')
screen.bgcolor("black")

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

turtleYpos = 480

COLOR_MAP = {
    "red": "#ff3333",
    "green": "#33ff33",
    "blue": "#3399ff",
    "yellow": "#ffff33",
    "white": "#ffffff",
    "orange": "#ff9933",
    "purple": "#cc66ff",
    "grey": "#555555"
}

STYLE_MAP = {
    "bold": "bold",
    "italic": "italic",
    "underline": "underline",
    "normal": "normal"
}

def write(text, speed=0.01):
    global turtleYpos
    turtle.setpos(-950, turtleYpos)
    current_color = "white"
    current_style = "normal"
    turtle.color(current_color)

    parts = re.split(r'(@\w+-)', text)

    for part in parts:
        match = re.match(r'@(\w+)-', part)
        if match:
            code = match.group(1).lower()
            if code in COLOR_MAP:
                current_color = COLOR_MAP[code]
                turtle.color(current_color)
            elif code in STYLE_MAP:
                current_style = STYLE_MAP[code]
            continue

        for i in range(len(part)):
            ch = part[i]
            next_ch = part[i+1] if i + 1 < len(part) else ""
            turtle.write(ch, font=('Arial', 16, current_style))

            if ch in [".", "!"]:
                sleep(0.5)
            else:
                sleep(speed)

            if ch == "W":
                spacing = 20
            elif ch.isupper() and next_ch != " ":
                spacing = 12 if ch not in ["I"] else 6
            elif ch in ["l", "t", "r", "f", "i", "j", "'"]:
                spacing = 6
            elif ch in ["w", "m"]:
                spacing = 17
            else:
                spacing = 11

            turtle.forward(spacing)

    _, y = turtle.position()
    turtleYpos = y - 30

askoutput = ""

def ask(txt, speed=0.01):
    write(txt, speed)
    return askstring('input', 'enter input')

def howto():
    print("Thank you for using better console by tobble © 2025.")
    print("----------------------------------------")
    print("To print text, use 'betterconsole.write(text, speed)'.")
    print("To take an input, use 'betterconsole.ask(text, speed)'.")
    print("----------------------------------------")
    print("To use colours and styles in text, use '@colour-' or '@style-'")
    print("----------------------------------------")
    print("Colours: @red-, @orange-, @yellow-, @green-, @blue-, @purple-, @white-, @grey-.")
    print("styles: @bold-, @italic-, @underline-, @normal-.")
    
howto()
write("@grey-Better console by tobble. © 2025.", 0)
turtle.clear()
turtleYpos = 480
