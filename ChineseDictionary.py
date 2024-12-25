from psychopy import visual, event, core
import random

# Create a window
win = visual.Window(size=(800, 600), color='white', units='pix')

# Create text stimuli for instructions and responses
instruction_text = visual.TextStim(win, text='Type a question and press Enter. Determine if the response is human or machine.', color='black', pos=(0, 250))
response_text = visual.TextStim(win, text='', color='black', pos=(0, 0))
input_text = visual.TextStim(win, text='', color='black', pos=(0, -100))
feedback_text = visual.TextStim(win, text='', color='black', pos=(0, -200))

# Simulated Chinese dictionary
chinese_dict = {
    "你好": "你好！有什么我可以帮你的吗？",
    "你是谁": "我是一个人工智能程序。",
    "今天天气怎么样": "今天的天气很好，适合外出。",
    "你会做什么": "我可以回答你的问题，告诉你一些信息。",
    "再见": "再见！"
}

# Function to simulate human-like or dictionary-based responses
def generate_response(question):
    if random.choice([True, False]):
        # Simulate human-like response
        responses = ["这是一个很好的问题。", "我不确定，但我会尽力回答。", "这很有趣，让我想一想。"]
        return random.choice(responses)
    else:
        # Use Chinese dictionary for responses
        return chinese_dict.get(question, "对不起，我不明白你的问题。")

# Main loop to display the interface and handle user input
user_input = ''
while True:
    # Draw the instruction and input text
    instruction_text.draw()
    input_text.draw()
    response_text.draw()
    feedback_text.draw()
    
    # Flip the window to update the display
    win.flip()
    
    # Capture user keypresses
    keys = event.getKeys()
    
    for key in keys:
        if key == 'return':
            # Generate and display a response
            response = generate_response(user_input)
            response_text.text = f'Response: {response}'
            user_input = ''  # Clear the input for the next question
        elif key == 'escape':
            # Exit the loop if 'escape' is pressed
            win.close()
            core.quit()
        elif key == 'backspace':
            # Handle backspace for text input
            user_input = user_input[:-1]
        else:
            # Add the key to the input string
            user_input += key
    
    # Update the input text display
    input_text.text = f'Input: {user_input}'

# Close the window
win.close()
core.quit()
