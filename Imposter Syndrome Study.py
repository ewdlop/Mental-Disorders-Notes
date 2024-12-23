from psychopy import visual, event, core, gui

# Create a window
win = visual.Window(size=(800, 600), color=(1, 1, 1), fullscr=False)

# Create an introduction text
intro_text = visual.TextStim(win, text="Welcome to the Imposter Syndrome Study!\n\n"
                                       "You will be presented with a series of tasks.\n"
                                       "After each task, you will rate your confidence and perceived competence.\n\n"
                                       "Press any key to continue.", color=(-1, -1, -1))
intro_text.draw()
win.flip()
event.waitKeys()

# List of tasks
tasks = [
    "Task 1: Solve the math problem 3 + 5",
    "Task 2: Solve the math problem 7 - 2",
    "Task 3: Solve the math problem 6 * 4"
]

# Function to display a task and get ratings
def run_task(task_text):
    task_stim = visual.TextStim(win, text=task_text, color=(-1, -1, -1))
    task_stim.draw()
    win.flip()
    event.waitKeys()

    # Confidence rating
    confidence_rating = gui.DlgFromDict({"Confidence (1-10)": "5"}, title="Confidence Rating")
    if confidence_rating.OK:
        confidence = confidence_rating.data[0]
    else:
        core.quit()

    # Competence rating
    competence_rating = gui.DlgFromDict({"Competence (1-10)": "5"}, title="Competence Rating")
    if competence_rating.OK:
        competence = competence_rating.data[0]
    else:
        core.quit()

    return confidence, competence

# Run tasks and collect ratings
results = []
for task in tasks:
    confidence, competence = run_task(task)
    results.append((task, confidence, competence))

# Display results
result_text = "Results:\n"
for task, confidence, competence in results:
    result_text += f"{task}\nConfidence: {confidence}, Competence: {competence}\n\n"

result_stim = visual.TextStim(win, text=result_text, color=(-1, -1, -1))
result_stim.draw()
win.flip()

# Wait for a key press to end
event.waitKeys()

# Close the window
win.close()
core.quit()
