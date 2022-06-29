#!/usr/bin/env python3
import os
from typing import Tuple, Union
from selenium import webdriver
from selenium.webdriver.common.by import By

from database_handler import DatabaseHandler


class PedantixInterface:

    def __init__(self, database: DatabaseHandler) -> None:
        drivers_path = os.path.join(os.getcwd(), "drivers")
        os.environ["PATH"] += os.pathsep + drivers_path

        self.database = database

        self.browser = webdriver.Firefox()
        self.browser.get("https://cemantix.herokuapp.com/pedantix")

        self.guess_area = self.browser.find_element(By.ID, 'guess')
        self.guess_button = self.browser.find_element(By.ID, 'guess-btn')
        self.dial_close = self.browser.find_element(By.ID, 'dialog-close')
        self.error_field = self.browser.find_element(By.ID, 'error')

        self.dial_close.click()

    def validate(self, word: str) -> Union[Tuple[int, int], None]:
        """
        Method that tries the sent word in pedantix and that returns the number of green and oranges. Returns None if word doesn't exist.
        :return: (greens, oranges) or None
        """
        self.guess_area.send_keys(word)
        self.guess_button.click()

        errors = self.error_field.text

        greens = errors.count('🟩')
        oranges = errors.count('🟧')

        if greens + oranges > 0 or errors.count('🟥'):
            return (greens, oranges)
        else:
            return None

    def manual_tries(self):

        print("Guess the word")
        while True:
            user_guess = input(" - ")

            validation = self.validate(user_guess)
            if validation is not None:
                self.database.insert_word(user_guess, validation[0], validation[1])

            print(f'{validation[0]} greens and {validation[1]} oranges')

