from pynput.keyboard import Key, KeyCode, Listener

# Your functions

def function_1():
    print('Executed function_1')

def function_2():
    print('Executed function_2')

# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset([Key.shift, KeyCode(char='a')]): function_1, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.shift, KeyCode(char='A')]): function_1,
    frozenset([Key.shift, KeyCode(char='b')]): function_2,
    frozenset([Key.shift, KeyCode(char='B')]): function_2,
}

# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    current_keys.remove(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()