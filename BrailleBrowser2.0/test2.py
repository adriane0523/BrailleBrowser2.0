from pynput.keyboard import Key, Listener
from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='o')},
    {keyboard.Key.ctrl_r, keyboard.KeyCode(char='z')},    
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='x')},    
    {keyboard.Key.ctrl_r, keyboard.KeyCode(char='x')}
]

# The currently active modifiers
current = set()

def execute():
    print("Here I am")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:          
        # Stop listener
        return False

    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)



rate = engine.getProperty('rate')
engine.setProperty('rate', rate+150)
driver.get("https://www.google.com/")
engine.say('Opening Google.com')
engine.runAndWait() 

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()