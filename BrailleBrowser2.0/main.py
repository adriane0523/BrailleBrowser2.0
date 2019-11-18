import msvcrt
import os
import signal
import threading
import time
import webbrowser
from urllib.request import Request, urlopen

import pyttsx3
import serial
import speech_recognition as sr
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import keyboard
from pyfirmata import Arduino, util

sr.__version__

def arduino(input):
    board = Arduino("COM10")

        
        
def getLink(link):

    result = 0
    index = 0
    for i in link:
        if i == "&" and link[index + 1] == "s" and link[index+ 2] or( i == "%" and link[index + 1] == "3"):
            result = index
            break
        index = index + 1


    return result

def recongize_speech_from_mic(recongizer, mic):

    if not isinstance(recongizer, sr.Recognizer):
        raise TypeError("recognizer must be recongizer instance")
    
    if not isinstance(mic, sr.Microphone):
        raise TypeError("microphone must be microphone instance")

    with mic as source:
        recongizer.adjust_for_ambient_noise(source)
        audio = recongizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recongizer.recognize_sphinx(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unvailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recongize speech"
    
    return response

def speak(r, mic):
    print("Start Speaking")
    result = ""
    for i in range(50):
        command = recongize_speech_from_mic(r,mic)

    
        if command["transcription"]:
            print (command["transcription"])
            result = command["transcription"] + ""
            break
        if not command["success"]:
            break
        print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if command["error"]:
            print("ERROR: {}".format(command["error"]))
            break

        # show the user the transcription
        print("You said: {}".format(command["transcription"]))

    print("Stop Speaking")
    print("PROGRAM HEARD:",result)
    return result


def search(keyword, driver):
    links = []

    search= driver.find_element_by_name('q')
    search.send_keys(keyword)

    opretAnnonce = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')
    opretAnnonce.send_keys(Keys.RETURN)
    currentUrl = driver.current_url
    req = Request(currentUrl, headers={'User-Agent': 'Chrome'})

    req = driver.current_url()
    webpage = urlopen(req).read()

    page_soup = soup(webpage, "html.parser")
    searchResults = page_soup.find_all(id="search")


    
    for item in page_soup.find_all('h3', attrs={'class' : 'r'}):
        endIndex = getLink(item.a['href'])
        newLink = item.a['href'][7:endIndex]
        links.append(newLink)

    return links
        
def repeatLinks(links,engine):
     for i in range(3):
        engine.say(links[i])
        engine.runAndWait()


def keyboard_listener(engine):
    keys = ['a','b','c','d','e','f','g','h','i','j','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while True:  # making a loop
        i = 0
        flag = True
        if keyboard.is_pressed('a'):
            engine.say('a')
            break

        
            
        

        comment = """
        while(flag and i < len(keys)):
            if keyboard.is_pressed(keys[i]):
                print('You pressed', keys[i])
                engine.say(keys[i])
                flag = False

            i = i + 1
            """
               
                    
r = sr.Recognizer()
mic = sr.Microphone()
driver = webdriver.Chrome(executable_path=r'C:\Users\adria\OneDrive\Desktop\chromedriver_win32 (1)\chromedriver.exe')
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+150)
driver.get("https://www.google.com/")
engine.say('Opening Google.com')
engine.runAndWait() 
userInput = ""




while (userInput != "x"):
    

    
    links = []
    
    menu = """
    type 'v' to use mic
    type 'c' to use keyboard
    """
    print(menu)
    engine.say(menu)
    engine.runAndWait()

   
    userInput = input("> ")

    if (userInput == "q"):

        while(userInput != "@"):
            userInput = input("> ")
     
            arduino(userInput)




    if (userInput == "c"):
        engine.say("Start typing to search")
        engine.runAndWait()

        #t1 = threading.Thread(target=keyboard_listener, args=(engine,)) 
        #t1.start() 

        searchInput= input("> ")
        links = search(searchInput, driver)
        search = "searchng " + searchInput
        engine.say(search)
        repeatLinks(links,engine)


       
        openLink = input("> ")

        


        driver.get(links[(int)(openLink)])
        
        uClient = urlopen(links[(int)(openLink)])
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        container = page_soup.find('body')


        
        result = ""
        
        for div in container.find_all('div'):
            result = result + (str)(div.text)

        result = result.strip(' \n\t')
        print (result)

        engine.say(result)
        engine.runAndWait()

        comment = """
        for i in result:
            print(i)
            arduino(i.lower())
            engine.say(i)
            engine.runAndWait()
            time.sleep(1)
            """
            

    
    if (userInput == "v"):
        engine.say("Start Talking")
        engine.runAndWait() 
        speech = speak(r,mic)

        print(speech[0:6])
        if (speech[0:6] == "search"):

            search(speech[6:len(speech)], driver)
            repeatLinks(links,engine)
                
            

        if (speech[0:4] == "open"):
            number = -1
            if (speech[5:] == "one"):
                number = 1
            elif (speech[5:] == "two"):
                number = 2
            elif(speech[5:]) == "three":
                number = 3
            elif(speech[5:] == "four"):
                number = 4
            elif (speech[5:] == "five"):
                number = 5
            

            driver.get(links[number])

            page = urllib2.urlopen(links[number]).read()
            soup = BeautifulSoup(page)
            body = soup.find('body')
            the_contents_of_body_without_body_tags = body.findChildren()

            print(the_contents_of_body_without_body_tags)
