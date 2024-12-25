from psychopy import visual, event, core
import random

# Function to simulate random decision making
def random_decision():
    return random.choice(['yes', 'no'])

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# Create buttons and text for the Turing test
decision_button = visual.Rect(win, width=150, height=50, fillColor='blue', pos=(0, 100))
decision_text = visual.TextStim(win, text='Make Decision', color='white', pos=(0, 100))

result_text = visual.TextStim(win, text='', color='black', pos=(0, 0))
instruction_text = visual.TextStim(win, text='Press the button to simulate a decision.', color='black', pos=(0, -200))

# Main loop to display the buttons and check for clicks
while True:
    # Draw the decision button and instructions
    decision_button.draw()
    decision_text.draw()
    instruction_text.draw()
    result_text.draw()
    
    # Flip the window to update the display
    win.flip()

    # Check for mouse clicks
    mouse = event.Mouse(win=win)
    if mouse.isPressedIn(decision_button):
        # Simulate random decision making
        decision = random_decision()
        result_text.text = f'Decision: {decision}'
        core.wait(0.3)  # Debounce the button press

    # Check for keypresses to exit
    keys = event.getKeys()
    if 'escape' in keys:
        break

# Close the window
win.close()
core.quit()
