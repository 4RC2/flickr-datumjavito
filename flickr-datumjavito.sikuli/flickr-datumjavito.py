# [✓] Go to next item when you save?

while True:
    click(Location(740, 240)) # Date taken
    sleep(0.5) 
    type("a",KEY_CTRL)
    type("c",KEY_CTRL)
    
    click(Location(876, 446)) # away
    
    click(Location(740, 350)) # Date uploaded
    sleep(0.5) 
    type("a",KEY_CTRL)
    type(Key.BACKSPACE)
    type("v",KEY_CTRL)
    
    click(Location(876, 446)) # away
    
    click(Location(920, 240)) # Time taken
    sleep(0.5)
    type("a",KEY_CTRL)
    type("c",KEY_CTRL)
    
    click(Location(920, 350)) # Time uploaded
    sleep(0.5)
    type("a",KEY_CTRL)
    type(Key.BACKSPACE)
    type("v",KEY_CTRL)

    wait("1487528292864.png") 
    click("1487528292864.png") # Save button
    wait("1487528364338.png")