import time
import pyautogui


def get_number(text_message, data_type, exception_type=ValueError):
    while True:
        user_input = input(text_message)
        try:
            num_input = data_type(user_input)
            return num_input
        except exception_type:
            print('This is no valid input')
            continue


def indent(lines):
    for line in range(lines):
        pyautogui.press('home')
        pyautogui.press('down')
        pyautogui.press('tab')
