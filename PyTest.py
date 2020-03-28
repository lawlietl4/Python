# I need to make an automation script that is python and will do what I need
import keyboard
import time

myint = 0

while(myint < 365):
    myint += 1
    time.sleep(5)
    keyboard.write('sudo ifconfig eth0 down')
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.write('1234')
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.write('sudo ifconfig eth0 up')
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.write('sudo ifconfig eth1 down')
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.write('sudo ifconfig eth1 up')
    keyboard.press_and_release('enter')
    time.sleep(86400)
else:
    keyboard.write('restart loop as I made this to only loop for a year after deployment')