#   libraries
import os
import logging
import win32gui
import cv2
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
#   local libraries
import grabscreen

#   Global Variables
dino_game_url = 'chrome://dino/'
target_window_name = r'chrome://dino/ - Google Chrome'
driver = None
window = None

#   Open Dino runner game in chrome
def open_game():
    global driver
    driver_path = os.path.dirname(os.path.abspath(__file__)) + '\chromedriver.exe'
    driver = webdriver.Chrome(driver_path)
    driver.get(dino_game_url)
    driver.set_window_size(1024, 512)
    # return driver

#   returns the image of the game given a window
def get_screen():
    window = win32gui.FindWindow(None, target_window_name)

    window_dimensions = win32gui.GetWindowRect(window)

    #   adjust dimensions edges to ignore browser toolbar and capture borders
    toolbar_height = 135
    left_border = 10
    bottom_border = 10
    right_border = 10
    window_dimensions = (
    window_dimensions[0] + left_border,
    window_dimensions[1] + toolbar_height,
    window_dimensions[2] - right_border,
    window_dimensions[3] - bottom_border)

    # grabbed_image = grabscreen.grab_screen(region=(0, 40, 1920, 1120))
    img = grabscreen.grab_screen(window_dimensions)
    #grabbed_image  = cv2.resize(grabbed_image, (480, 270))

    #   convert to RGB image:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    return img

#   Returns windows focused state of dino game
def is_game_focused():
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == target_window_name:
        return True
    else:
        return False

#   returns true if brower is alive
def is_game_running():
    global driver
    try:
        driver.title
        return True
    except WebDriverException:
        return False

#   closes browser game
def close_game():
    global driver
    driver.quit()
