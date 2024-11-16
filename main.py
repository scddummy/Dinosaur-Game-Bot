import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time

DINO_URL = "https://elgoog.im/t-rex/"
BEGIN_TIME = time.time() + 8


class Dinosaur:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--window-size=1900,1000")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def load_game(self):
        self.driver.get(DINO_URL)
        time.sleep(8)
        screen = self.driver.find_element(By.TAG_NAME, value="body")
        screen.send_keys(Keys.UP)

    def take_screenshot(self):
        seconds_elapsed = time.time() - BEGIN_TIME
        if seconds_elapsed < 12:
            im = pyautogui.screenshot(region=(425, 650, 100, 100))
        elif 12 <= seconds_elapsed < 22:
            im = pyautogui.screenshot(region=(435, 650, 100, 100))
        elif 22 <= seconds_elapsed < 32:
            im = pyautogui.screenshot(region=(455, 650, 100, 100))
        else:
            im = pyautogui.screenshot(region=(480, 650, 100, 100))
        im2 = im.convert("P", palette=Image.ADAPTIVE, colors=256)
        return im2.getpalette()

    def check_jump(self, palette):
        if palette != [255, 255, 255]:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.UP)
            actions.perform()
            print("yes")


bot = Dinosaur()
bot.load_game()

t = True
while t:
    current_palette = bot.take_screenshot()
    bot.check_jump(current_palette)


