from pynput import keyboard

import msvcrt
import os
import signal
import threading
import time
import webbrowser


import pyttsx3
import serial
import speech_recognition as sr
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading

from pyfirmata import Arduino, util

import json

sr.__version__4
if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    

  
    user_input = ""
    while (user_input != "x"):
        user_input = input(">")


        if (user_input == "o"):

            driver.get("https://www.google.com/")
                
        if ( user_input == "v"):
            
            
           
            uClient = urlopen((str)(driver.current_url))
            page_html = uClient.read()
            uClient.close()

            

            page_soup = soup(page_html, "html.parser")
            container = page_soup.find('body')
            
            result = ""
            
            for div in container.find_all('div'):
                result = result + (str)(div.text)




            flag = True
            start = 0
            end = 3
            result = result.strip(' \n\t')

            data = {"letters":[
                {
                    "letter": "0",
                    "shift": 14
                },
                {
                    "letter": "1",
                    "shift": 1
                },
                {
                    "letter": "2",
                    "shift": 5
                },
                {
                    "letter": "3",
                    "shift": 3
                },
                {
                    "letter": "4",
                    "shift": 11
                },
                {
                    "letter": "5",
                    "shift": 9
                },
                {
                    "letter": "6",
                    "shift": 7
                },
                {
                    "letter": "7",
                    "shift": 15
                },
                {
                    "letter": "8",
                    "shift": 13
                },
                {
                    "letter": "9",
                    "shift": 9
                },
                {
                    "letter": "a",
                    "shift": 1
                },
                {
                    "letter": "b",
                    "shift": 5
                },
                {
                    "letter": "c",
                    "shift": 3
                },
                {
                    "letter": "d",
                    "shift": 11
                },
                {
                    "letter": "e",
                    "shift": 9
                },
                {
                    "letter": "f",
                    "shift": 7
                },
                {
                    "letter": "g",
                    "shift": 15
                },
                {
                    "letter": "h",
                    "shift": 13
                },
                {
                    "letter": "i",
                    "shift": 6
                },
                {
                    "letter": "j",
                    "shift": 14
                },
                {
                    "letter": "k",
                    "shift": 17
                },
                {
                    "letter": "l",
                    "shift": 21
                },
                {
                    "letter": "n",
                    "shift": 27
                },
                {
                    "letter": "o",
                    "shift": 25
                },
                {
                    "letter": "p",
                    "shift": 23
                },
                {
                    "letter": "q",
                    "shift": 31
                },
                {
                    "letter": "r",
                    "shift": 29
                },
                {
                    "letter": "s",
                    "shift": 41
                },
                {
                    "letter": "t",
                    "shift": 30
                },
                {
                    "letter": "u",
                    "shift": 5
                },
                {
                    "letter": "v",
                    "shift": 49
                },
                {
                    "letter": "w",
                    "shift": 46
                },
                {
                    "letter": "x",
                    "shift": 51
                },
                {
                    "letter": "y",
                    "shift": 59
                },
                {
                    "letter": "z",
                    "shift": 61
                }
                ]
            }
           

            comment = '''
            send_b = 0b000000
            mutiplier = 1
            while(end < 500):
                
                send = ""
                temp = 0b000000
                for i in range(start,end):
                    print(result[i])

                    for c in data["letters"]:
                        if c["letter"] == result[i]:

                            x = c["shift"]
                            temp = temp | x

                     
                    send_b = send_b | temp
                    send_b = send_b << 6
                    send = send + result[i] 
                    temp = 0b000000
                    time.sleep(1)
            
                send_b = 0b000000
                



               

                start = start + 3
                end = end + 3
                send = ""
                '''    
            
                #print("{0:b}".format(send_b))
            
          
          
            print (result)



   



