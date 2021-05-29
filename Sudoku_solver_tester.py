import time

import pyautogui


def sudoku_test():
    time.sleep(3)
    pyautogui.press('9')
    pyautogui.press('enter')

    def zero():
        pyautogui.press('0')
        pyautogui.press('enter')

    def one():
        pyautogui.press('1')
        pyautogui.press('enter')

    def two():
        pyautogui.press('2')
        pyautogui.press('enter')

    def three():
        pyautogui.press('3')
        pyautogui.press('enter')

    def four():
        pyautogui.press('4')
        pyautogui.press('enter')

    def five():
        pyautogui.press('5')
        pyautogui.press('enter')

    def six():
        pyautogui.press('6')
        pyautogui.press('enter')

    def seven():
        pyautogui.press('7')
        pyautogui.press('enter')

    def eight():
        pyautogui.press('8')
        pyautogui.press('enter')

    def nine():
        pyautogui.press('9')
        pyautogui.press('enter')

    zero()
    nine()
    six()
    one()
    five()
    zero()
    eight()
    zero()
    zero()

    zero()
    zero()
    eight()
    zero()
    zero()
    six()
    seven()
    four()
    five()

    zero()
    zero()
    zero()
    zero()
    eight()
    four()
    zero()
    nine()
    six()

    nine()
    zero()
    zero()
    zero()
    zero()
    zero()
    three()
    seven()
    zero()

    zero()
    zero()
    four()
    nine()
    two()
    zero()
    zero()
    zero()
    zero()

    zero()
    eight()
    five()
    zero()
    zero()
    zero()
    four()
    two()
    zero()

    eight()
    zero()
    zero()
    five()
    four()
    zero()
    six()
    one()
    three()

    zero()
    three()
    zero()
    six()
    zero()
    two()
    nine()
    eight()
    zero()

    zero()
    four()
    nine()
    zero()
    three()
    zero()
    zero()
    zero()
    zero()


sudoku_test()
