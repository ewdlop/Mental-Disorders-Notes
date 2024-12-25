from psychopy import visual, event, core

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# Create the "erase memory" button
erase_button = visual.Rect(win, width=150, height=50, fillColor='red', pos=(0, 0))
erase_text = visual.TextStim(win, text='Erase Memory', color='white', pos=(0, 0))

# Simulated memory to be erased
memory = ["item1", "item2", "item3"]

# Function to handle button click
def erase_memory():
    global memory
    memory.clear()
    print("Memory erased")

# Main loop to display the button and check for clicks
while True:
    # Draw the button and text
    erase_button.draw()
    erase_text.draw()

    # Flip the window to update the display
    win.flip()

    # Check for mouse clicks
    mouse = event.Mouse(win=win)
    if mouse.isPressedIn(erase_button):
        erase_memory()
        core.wait(0.3)  # Debounce the button press

    # Check for keypresses to exit
    keys = event.getKeys()
    if 'escape' in keys:
        break

# Close the window
win.close()
core.quit()
