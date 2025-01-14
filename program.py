from pynput.mouse import Controller, Button

from pynput.keyboard import Controller as KeyboardController, Key
import pyperclip

import time
from openai import OpenAI
import re
client = OpenAI(api_key="enter your API key")


def is_message_from_sender(chat_log,sender_name="write the sender name correctly"):
    messages=chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True
    return False
mouse = Controller()
keyboard = KeyboardController()

mouse.position = (1208, 4)
mouse.click(Button.left)
time.sleep(2)  # Ensure the click is registered

# Step 2: Move the cursor to (762, 213) and click, then type "safari" and press Enter
mouse.position = (762, 213)
mouse.click(Button.left)
time.sleep(1)  # Wait for the click to register

# Typing "safari" and pressing Enter using keyboard controller
keyboard.type("safari")
keyboard.press(Key.enter)  # Use Key.enter to press the Enter key
keyboard.release(Key.enter)
time.sleep(5)  # Wait for Safari to load

while True:
    

    # Step 3: Move to the search bar or window at (528, 167) and click
    mouse.position = (528, 167)
    mouse.click(Button.left)
    time.sleep(1)  # Wait for the click to register

    # Step 4: Start dragging from (528, 167) to (911, 807) to select text
    mouse.position = (528, 167)
    mouse.press(Button.left)  # Hold down the mouse button to start selection
    time.sleep(0.5)  # Slight pause to simulate real behavior

    # Dragging smoothly to the target location
    mouse.position = (911, 807)  # Move the cursor to the end point
    time.sleep(0.5)  # Allow time for the drag to complete
    mouse.release(Button.left)  # Release the mouse button to finish the selection
    time.sleep(1)  # Wait for the selection to finalize

    # Step 5: Press 'Command + C' to copy the selected text (macOS shortcut)
    keyboard.press(Key.cmd)
    keyboard.press('c')
    keyboard.release(Key.cmd)
    keyboard.release('c')
    time.sleep(2)  # Wait for the clipboard to update
    mouse.click(Button.left)

    # Step 6: Retrieve the copied content from the clipboard
    copied_content = pyperclip.paste()

    # Step 7: Print the copied content
    print("Copied content:", copied_content)

    # Final output
    print("The copied data is:", copied_content)

    if is_message_from_sender(copied_content):
        def openaitool(copied_data):
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a person name Utkarsh who speaks english as well as hindi he is from india and he is a coder . you analyse chat history and response (message only) and remove ChatCompletionMessage(content=' "},
                    {
                        "role": "user","content": copied_data
                    }
                ]
            )
            response_text=completion.choices[0].message.content
            print("Response from OpenAI:", response_text)

            pyperclip.copy(response_text)
            print("Response copied to clipboard.")
            return response_text
        def automate_task2(response):
            mouse = Controller()
            keyboard = KeyboardController()
            mouse.position = (762,858)
            mouse.click(Button.left)
            time.sleep(1)  # Ensure the click is registered

            # Step 2: Press 'Command + V' to paste the content (macOS shortcut)
            keyboard.press(Key.cmd)  # Hold Command (⌘) key
            keyboard.press('v')  # Press 'v' key to paste
            keyboard.release(Key.cmd)  # Release Command (⌘) key
            keyboard.release('v')  # Release 'v' key
            time.sleep(2)
            
            print("data pasated",response)
            mouse.position = (1397,863)
            mouse.click(Button.left)
            return response   
            
        if __name__ == "__main__":
            response = openaitool(copied_content)
            print("The pasted data is:", response)
            automate_task2(response)