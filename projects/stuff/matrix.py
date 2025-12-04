import betterConsole as bc
from time import sleep
import random

bc.customise(bgCol="black", title="Matrix Loader V4")

bc.write("@green-@bold-Matrix Loader V4 Boooting...",0.05)
bc.write("@green-Main Bootstrap Loading...",0.01)
bc.write("@green-loading main kernel...",0.05)
bc.write("@green-Loading file system...",0.01)
sleep(1)

usr = bc.ask("@green-Username:")

if usr != "gerd":
    bc.write("@red-@bold-@underlined-!NO!")
    bc.byebye()

pswd = bc.ask("@green-Enter Password")

if pswd != "1234":
    bc.write("@red-@bold-@underlined-!NO!")
    bc.byebye()

bc.reset()
bc.write("@green-@bold-Welcome To The Matrix")
