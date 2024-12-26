from psychopy import visual, core, event

# Create a window
win = visual.Window([800, 600], color=(1, 1, 1))

# Define gradient colors
colors = [
    [1, 0, 0],  # Red
    [1, 1, 0],  # Yellow
    [0, 1, 0],  # Green
    [0, 1, 1],  # Cyan
    [0, 0, 1],  # Blue
    [1, 0, 1],  # Magenta
]

# Create a circular stimulus with gradient colors
stimulus = visual.RadialStim(
    win,
    tex='sqrXsqr',
    color=colors,
    size=1.5,
    radialCycles=2,
    angularCycles=2,
    radialPhase=0.5,
    angularPhase=0.5,
    interpolate=True,
)

# Draw the stimulus and update the window
stimulus.draw()
win.flip()

# Wait for a key press to close
event.waitKeys()

# Close the window
win.close()
core.quit()
