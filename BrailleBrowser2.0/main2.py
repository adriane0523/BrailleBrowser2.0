from pynput import keyboard






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
    comment = '''
    elif (input is "z"):
        board.digital[13].write(0)
        board.digital[12].write(1)
        board.digital[11].write(1)
        board.digital[10].write(0)
        board.digital[7].write(0)
        board.digital[6].write(0)
    '''    
    
def search(keyword, driver):
    links = []

    search= driver.find_element_by_name('q')
    search.send_keys(keyword)

    opretAnnonce = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')
    opretAnnonce.send_keys(Keys.RETURN)
    currentUrl = driver.current_url
    req = Request(currentUrl, headers={'User-Agent': 'Chrome'})
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
               
                    


userInput = ""


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.get("https://www.google.com/")

    if(driver.findElement(By.xpath("//*[@id='someID']")).isDisplayed()){
    String previousURL = driver.getCurrentUrl();
    driver.findElement(By.xpath("//*[@id='someID']")).click();  
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

    ExpectedCondition e = new ExpectedCondition<Boolean>() {
          public Boolean apply(WebDriver d) {
            return (d.getCurrentUrl() != previousURL);
          }
        };

    wait.until(e);
    currentURL = driver.getCurrentUrl();
    System.out.println(currentURL);
} 
sha


def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener

    if k in ['shift', 'o']: # keys interested
        # self.keys.append(k) # store it in global-like variable
        print('Key pressed: ' + k)

    
#lis = keyboard.Listener(on_press=on_press)
#lis.start() # start to listen on a separate thread
#lis.join() # no this if main thread is polling self.keyaa122


def hello():
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
