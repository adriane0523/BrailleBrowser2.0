import json
import serial
import time

from bs4 import BeautifulSoup as soup
from selenium import webdriver
from urllib.request import Request, urlopen
from pynput.keyboard import Key, KeyCode, Listener



def Arduino(word, ser):
    # Serial write section
    data = read_json()
    count = 0

    while (count < 2):
        for i in data["letters"]:
            if (word[count] == i["letter"]):
                ser.write(chr(i["shift"]).encode())
                time.sleep(2) # with the port open, the response will be buffered 
                            # so wait a bit longer for response here
                ser.flush()
                break
        count = count + 1


    read = """
    # Serial read section
    msg = ser.read(ser.inWaiting()) # read everything in the input buffer
    print ("Message from arduino: ")
    print (msg)
    """

    



# Your functions
driver = None
def function_1():
    print('Executed function_1')

    driver.get("https://www.google.com/")
   


def function_2():
    print('Executed function_2')
    uClient = urlopen((str)(driver.current_url))
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    container = page_soup.find('body')

    result = ""

    for div in container.find_all('div'):
        result = result + (str)(div.text)

    result = result.strip(' \n\t')
    result = result.lower()
    print(result)


    ser = serial.Serial('COM4', 9600)
    index = 0
    while (index < len(result)-1):
        send = result[index] + result[index + 1]
        print(send)
        Arduino(send,ser)
        time.sleep(3)
        index = index + 2

def read_json():
    
    with open('data.json',"r") as json_file:
        data = json.load(json_file)
        return data

    return None

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



if  __name__ == "__main__":

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

   