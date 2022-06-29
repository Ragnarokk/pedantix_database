#!/usr/bin/env python3
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from database_handler import DatabaseHandler


def pedantix_interface():
    drivers_path = os.path.join(os.getcwd(), "drivers")
    os.environ["PATH"] += os.pathsep + drivers_path

    browser = webdriver.Firefox()
    browser.get("https://cemantix.herokuapp.com/pedantix")

    guess_area = browser.find_element(By.ID, 'guess')
    guess_button = browser.find_element(By.ID, 'guess-btn')
    dial_close = browser.find_element(By.ID, 'dialog-close')
    error_field = browser.find_element(By.ID, 'error')

    dial_close.click()

    print("Guess the word")
    while True:
        user_guess = input(" - ")

        guess_area.send_keys(user_guess)
        guess_button.click()

        errors = error_field.text

        greens = errors.count('🟩')
        oranges = errors.count('🟧')

        print(f'{greens} greens and {oranges} oranges')


if __name__ == '__main__':
    DatabaseHandler()
    pedantix_interface()
