import pyautogui
import keyboard
import autoclicker

print("Bienvenido maestro San porfavor presione f6 para activar y k para desactivar el autoclicker")
def clicker1():
    presionar = False 
    while True:
        if keyboard.is_pressed('f6') and not presionar:
            presionar = True
            while presionar:
                pyautogui.click()
                if keyboard.is_pressed('f7'):
                    presionar = False
        elif keyboard.is_pressed('f7'):
            presionar = False

clicker1()
