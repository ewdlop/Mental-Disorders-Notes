from psychopy import visual, core, event

# Create a window
win = visual.Window(size=[800, 600], color=[1, 1, 1], units="pix")

# Create a red circle stimulus
circle = visual.Circle(win, radius=50, fillColor='red', lineColor='red')

# Draw the circle to the window
circle.draw()

# Flip the window to show the stimulus
win.flip()

# Wait for 2 seconds
core.wait(2)

# Close the window
win.close()

# Exit the program
core.quit()
