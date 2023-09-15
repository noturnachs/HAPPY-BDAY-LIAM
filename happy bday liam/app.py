from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import settings
import contextlib
from wonderwords import RandomSentence

with contextlib.redirect_stdout(None):
    import pygame
import os
from time import sleep

pygame.mixer.init()
mus_dir = os.getcwd() + r"\sounds\applepay.mp3"
pygame.mixer.music.load(mus_dir)

sentence = RandomSentence()


def random_msg():
    return sentence.sentence()


def spam():
    driver_path = "chromedriver.exe"
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("--headless=new")

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.messenger.com/")

        wait = WebDriverWait(driver, 30)

        email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
        passs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
        login = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]'))
        )

        person = "wingers"  # person to send msg to or Group
        try:
            email.send_keys("USER_NAME SA FB NA GAMITON")
            passs.send_keys("PASSWORD SA FB NA GAMITON")
            login.click()

        except Exception as e:
            print("An error occurred in login: ", e)

        def selectUser():
            userfind = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[contains(text(), '" + person + "')]")
                )
            )

            userfind.click()
            driver.refresh()
            time.sleep(5)

        selectUser()

        print("Initiating...")
        # user_name = "danny"
        with open(settings.script, "r") as f:
            lines = f.readlines()

        counter = 0
        for line in lines:
            selectUser()
            for i in range(settings.iterations):
                counter += 1
                print(f"{counter} Sending: {line}")
                actions = ActionChains(driver)

                actions.send_keys("@" + "liam mi")
                actions.send_keys(Keys.ENTER)
                sleep(float(2))
                actions.perform()

                # Type the message
                actions.send_keys(line)
                actions.send_keys(Keys.ENTER)
                actions.perform()

                pygame.mixer.music.play()

                sleep(float(settings.delay))

                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            user_input = input(
                "Do you want to continue sending same iteration? (y/n): "
            )
            if user_input.lower() == "n":
                break
    except:
        driver.quit()


if __name__ == "__main__":
    spam()
