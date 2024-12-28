from psychopy import visual, core, event

# Create a window
win = visual.Window([800, 600], color=(1, 1, 1))

# Create visual stimuli representing limbs
left_hand = visual.Rect(win, width=0.2, height=0.4, pos=(-0.3, 0), fillColor='blue')
right_hand = visual.Rect(win, width=0.2, height=0.4, pos=(0.3, 0), fillColor='red')

# Draw the stimuli
left_hand.draw()
right_hand.draw()

# Flip (update) the window to show the stimuli
win.flip()

# Wait for 5 seconds to simulate sensory perception
core.wait(5)

# Close the window
win.close()
