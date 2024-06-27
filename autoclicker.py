import pyautogui
import keyboard
import autoclicker


def clicker1():
    presionar = False 
    while True:
        if keyboard.is_pressed('s') and not presionar:
            presionar = True
            while presionar:
                pyautogui.click()
                if keyboard.is_pressed('k'):
                    presionar = False
        elif keyboard.is_pressed('k'):
            presionar = False

clicker1()