from psychopy import visual, core

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# List of messages to display
messages = [
    "Welcome to the experiment.",
    "Please pay attention to the following instructions.",
    "You will see a series of images.",
    "Try to remember as many details as possible.",
    "Good luck!"
]

# Display each message for a fixed duration
for message in messages:
    # Create a text stimulus for the message
    text_stim = visual.TextStim(win, text=message, color='black', pos=(0, 0))
    
    # Draw the text stimulus
    text_stim.draw()
    
    # Flip the window to update the display
    win.flip()
    
    # Wait for 3 seconds before displaying the next message
    core.wait(3)

# Close the window
win.close()
core.quit()
