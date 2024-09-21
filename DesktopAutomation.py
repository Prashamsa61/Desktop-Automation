from RPA.Desktop import Desktop

desktop = Desktop()

# Launching an Application
desktop.open_application("notepad.exe")

# Typing Text in a Field
desktop.type_text("Hello,World")
