#   Standard libraries
import os
import logging
#   3rd party libraries
from selenium import webdriver
#   local libraries

#   url of dino game
dino_game_url = 'chrome://dino/'

driver_path = os.path.dirname(os.path.abspath(__file__)) + '\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get(dino_game_url)