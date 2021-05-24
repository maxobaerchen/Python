import time
import pyautogui


def get_number():
    while True:
        num_input = input('How many lines do you want to indent? ([e]xit) ')
        if 'e' in num_input:
            return False
        print('Click one line above the first line..')
        try:
            num_input = int(num_input)
            return num_input
        except ValueError:
            print('This is no valid input')
            continue


def indent(lines):
    for line in range(lines):
        pyautogui.press('home')
        pyautogui.press('down')
        pyautogui.press('tab')


if __name__ == '__main__':
    number = get_number()
    if not number:
        pass
    else:
        for i in range(3, 0, -1):
            print(str(i), '..')
            time.sleep(1)
        indent(number)
