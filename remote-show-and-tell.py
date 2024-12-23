from psychopy import visual, event, core, gui

# Create a window
win = visual.Window(size=(800, 600), color=(1, 1, 1), fullscr=False)

# Create an introduction text
intro_text = visual.TextStim(win, text="Welcome to the 'Show and Tell' Activity!\n\n"
                                       "You will be asked to describe an object or idea.\n\n"
                                       "Press any key to continue.", color=(-1, -1, -1))
intro_text.draw()
win.flip()
event.waitKeys()

# Create a GUI for input
info = {"Description": ""}
dlg = gui.DlgFromDict(info, title="Show and Tell", order=["Description"])
if dlg.OK:
    description = info["Description"]
else:
    core.quit()

# Display the description
description_text = visual.TextStim(win, text=f"Your description:\n\n{description}", color=(-1, -1, -1))
description_text.draw()
win.flip()

# Wait for a key press to end
event.waitKeys()

# Close the window
win.close()
core.quit()
