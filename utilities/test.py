import subprocess

def set_brightness():
    subprocess.run(['osascript', '-e', 'tell application "System Events"', '-e', 'key code 113', '-e', 'end tell'])
    
    #subprocess.run(['osascript', '-e', 'tell application "System Events"', '-e', 'key code 145', '-e', 'end tell'])

# Test the function with a brightness value
set_brightness()  # Adjust the brightness value as needed
