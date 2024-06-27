import keyboard
def press_windows_key():
    keyboard.send('win')  # 'win' es el código para la tecla Windows

# Variable para evitar múltiples ejecuciones de la acción
is_windows_pressed = False

while True:
    if keyboard.is_pressed('a'):
        if not is_windows_pressed:
            press_windows_key()
            is_windows_pressed = True
    else:
        is_windows_pressed = False

    
    if True:
        keyboard.write('cmd')
    
    
        if True:
            keyboard.on_press('enter')

            if True:
                keyboard.write('mkdir comeme los huevos')

    if keyboard.is_pressed('g'):
        break 