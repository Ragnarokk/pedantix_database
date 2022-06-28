#!/usr/bin/env python3
import os
from selenium import webdriver


def pedantix_interface():
    drivers_path = os.path.join(os.getcwd(), "drivers")
    os.environ["PATH"] += os.pathsep + drivers_path

    browser = webdriver.Firefox()
    browser.get("https://cemantix.herokuapp.com/pedantix")
    print("Hello world !")


if __name__ == '__main__':
    pedantix_interface()
