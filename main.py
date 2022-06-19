from inputs import get_gamepad
import mouse
import pyautogui as pag


def main():
    virtual_keyboard_up = False
    x,y = mouse.get_position()
    speed = [0,0]
    wheel_speed = 0
    running = True
    events = get_gamepad()
    for event in events :
        #mettre le programme en pause si on appuie sur R1
        if event.code == "BTN_TR":
            running = not running
    while running:
        events = get_gamepad()
        for event in events:
            # bouger la souris avec le joystick gauche
            if event.code == "ABS_X" or event.code == "ABS_Y":
                if event.code == "ABS_X":
                    speed[0] = event.state/10000
                if event.code == "ABS_Y":
                    speed[1] = -event.state/10000
                x += speed[0]
                y += speed[1]
                mouse.move(x, y)
            #cliquer si on appuie sur A
            if event.code == "BTN_SOUTH":
                if event.state == 1:
                    mouse.click()
            #presser échap si on appuie sur B
            if event.code == "BTN_EAST":
                if event.state == 1:
                    pag.press("esc")                
            #controle de la molette via le joystick droit
            if event.code == "ABS_RY":
                wheel_speed = event.state/100000
                mouse.wheel(wheel_speed)
            #ctrl + C pour quitter avec Y
            if event.code == "BTN_NORTH":
                pag.hotkey("ctrl","c")
            
                
                
                
if __name__ == "__main__":
    while True:
        main()