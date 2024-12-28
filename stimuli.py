from psychopy import visual, sound, core

# Create a window
win = visual.Window([800, 600], color=(1, 1, 1))

# Create a text stimulus
message = visual.TextStim(win, text='Listen to the sound!', color=(-1, -1, -1))

# Create a sound stimulus
beep = sound.Sound('A', secs=1.0)

# Draw the text stimulus
message.draw()

# Flip (update) the window to show the text
win.flip()

# Play the sound
beep.play()

# Wait for the sound to finish
core.wait(1.0)

# Close the window
win.close()
