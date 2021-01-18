import os
import subprocess
import time
from gpiozero import Button
from signal import pause

noise_button = Button(23)

def start_noise():
    cmd = "vlc --loop ~/Downloads/mps/Deep\ White\ Noise\ with\ Binaural\ Beats\ for\ Sleep\ \|\ Delta\ Waves\ Sleeping\ Sound\ \|\ 10\ Hours.webm"
    #cmd = 'TMUX=; tmux new -s noise "echo playing; sleep 10"'
    #cmd = 'tmux new -s noise "echo playing; sleep 10"'
    #cmd = ['tmux', 'new', '-s', 'noise', '"echo playing; sleep 10"']
    #cmd = ["echo", "playing", ";", "sleep", "10"]
    #cmd = "echo playing; sleep 10"
    #p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return p

def stop_noise():
    cmd = "killall vlc"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return p

playing = False
def toggle_noise():
    if playing:
        print("Stopping")
        stop_noise()
        playing = False
    else:
        print("No process found, starting")
        start_noise()
        playing = True

noise_button.when_pressed = toggle_noise
pause()

## pyShutter.py
## Read Bluetooth Remote Shutter
## from /dev/input/event5 and /dev/input/event6
## filter for key down of ENTER and VOLUMNUP
##
## http://helloraspberrypi.blogspot.com/2020/06/detect-bluetooth-remote-shutter-ab.html
##
## Work on Python 3.5+
## For Reading events from multiple devices
## read https://python-evdev.readthedocs.io/en/latest/tutorial.html
#
#from evdev import InputDevice, categorize, ecodes
#import asyncio
#
#shutter = InputDevice('/dev/input/event0')
#
#EV_VAL_PRESSED = 1
#EV_VAL_RELEASED = 0
#KEY_ENTER = 28
#KEY_VOLUMNUP = 115
#
#print(shutter)
#print('=== Start ===')
#
#async def print_events(device):
#
#    async for event in device.async_read_loop():
#        if event.type == ecodes.EV_KEY:
#            if event.value == EV_VAL_PRESSED:
#                if event.value == EV_VAL_PRESSED:
#                    if event.code == KEY_ENTER:
#                        print('<ENTER> Pressed')
#                    elif event.code == KEY_VOLUMNUP:
#                        print('<VOLUMNUP> Pressed')
#                print(device.path, categorize(event), sep=': ')
#                print('---')
#
#asyncio.ensure_future(print_events(shutter))
#
#loop = asyncio.get_event_loop()
#loop.run_forever()
#
