import betterConsole as bc

bc.customise(title="better Console DEMO!", font="Arial")

bc.write("@instantOn-@test-@green-Welcome... To @instantOff-@yellow-better console!", 0.01)
bc.wait()
bc.write("@green-Better console is a module developed by @yellow-@bold-tobble.")
bc.write("@green-It is turtle based and can be used in the same way the normal console can just with more @italic-@orange-customisation!")
ask1 = bc.ask("@yellow-it can take inputs...")
bc.write(f"@green-You inputed @purple-@bold-{ask1}!")
bc.write("@green-Use 'f' strings ^^^^")
bc.customise(font="Comic Sans MS")
bc.write("@green-Change fonts (goofy comic sans!)")
bc.customise(font="Arial")
bc.write("@green-And @blue-@underline-so.@normal- @red-@bold-much. @purple-@italic-MORE!!!")

bc.hold()

