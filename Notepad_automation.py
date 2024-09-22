from RPA.Desktop import Desktop
import os
import time

"""
This script demonstrates desktop automation by:
1. Opening Notepad.
2. Typing a predefined text.
3. Taking a screenshot of the Notepad window.
4. Opening the screenshot for viewing.
5. Closing Notepad.
"""

# Initialize the desktop automation
desktop = Desktop()

# 1. Opening Notepad
notepad_process = desktop.open_application("notepad.exe")
time.sleep(1)

# 2. Typing Text Directly (without locator)
definition = (
    "Desktop is a cross-platform library for navigating and interacting with desktop environments. It can be used to automate applications through the same interfaces that are available to human users."
)

# Type the definition into Notepad
desktop.type_text(definition)
time.sleep(1)

# 3. Adding Additional Text
additional_text = "\n\nThis is an additional note about desktop automation."
desktop.type_text(additional_text)
time.sleep(5)
# 4. Taking a Screenshot
screenshot_path = "notepad_screenshot.png"
desktop.take_screenshot(screenshot_path)
print(f"Screenshot saved as {os.path.abspath(screenshot_path)}")

# 5. Opening the Screenshot
screenshot_viewer = os.startfile(screenshot_path)
time.sleep(2)


# 6. Closing Notepad
desktop.close_all_applications()
