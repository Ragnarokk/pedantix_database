#!/usr/bin/env python3
import os
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By


class PedantixInterface:

    def __init__(self) -> None:
        drivers_path = os.path.join(os.getcwd(), "drivers")
        os.environ["PATH"] += os.pathsep + drivers_path

        self.browser = webdriver.Firefox()
        self.browser.get("https://cemantix.herokuapp.com/pedantix")

        self.guess_area = self.browser.find_element(By.ID, 'guess')
        self.guess_button = self.browser.find_element(By.ID, 'guess-btn')
        self.dial_close = self.browser.find_element(By.ID, 'dialog-close')
        self.error_field = self.browser.find_element(By.ID, 'error')

        self.dial_close.click()

    def validate(self, word: str) -> Tuple[int, int]:
        """
        Method that tries the sent word in pedantix and that returns the number of green and oranges
        :return: (greens, oranges)
        """
        self.guess_area.send_keys(word)
        self.guess_button.click()

        errors = self.error_field.text

        greens = errors.count('🟩')
        oranges = errors.count('🟧')

        return (greens, oranges)

    def manual_tries(self):

        print("Guess the word")
        while True:
            user_guess = input(" - ")

            g, o = self.validate(user_guess)

            print(f'{g} greens and {o} oranges')

