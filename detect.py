import os
import subprocess
import time
from evdev import InputDevice, categorize, ecodes


class Shutter():
    def __init__(self):
        self.shutter_device = None

    def get_device(self):
        if self.shutter_device is None:
            print("Device connected")
            self.shutter_device = InputDevice('/dev/input/event0')
        return self.shutter_device

    def unset_device(self):
        self.shutter_device = None

shutter_instance = Shutter()

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
while True:
    if os.path.exists('/dev/input/event0'):
        try:
            shutter = shutter_instance.get_device()
            for event in shutter.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1 and event.code == 115:
                        print("pressed")
                        if playing:
                            print("Stopping")
                            stop_noise()
                            playing = False
                        else:
                            print("No process found, starting")
                            start_noise()
                            playing = True
                    elif event.value == 0 and event.code == 115:
                        print("released")
        except OSError:
            print("Device disconnected, sleeping")
            shutter_instance.unset_device()
            time.sleep(1)
        except IOError:
            print("Unknown IO Error, sleeping")
            shutter_instance.unset_device()
            time.sleep(1)
    else:
        time.sleep(1)

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
