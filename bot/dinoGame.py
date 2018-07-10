#   Standard libraries
import os
import logging
import time
#   3rd party libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#   local libraries
from directkeys import PressKey,ReleaseKey, SPACE, DOWN

#   url of dino game
dino_game_url = 'chrome://dino/'

#   Open the dino game in the chrome browser
driver_path = os.path.dirname(os.path.abspath(__file__)) + '\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get(dino_game_url)

#   Start game
#   Wait for X seconds since page has to load
time.sleep(2)

#   Find and focus chrome window

#   Press SPACE key to start
PressKey(SPACE)
ReleaseKey(SPACE)