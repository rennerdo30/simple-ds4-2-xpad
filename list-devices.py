#!/usr/bin/python3

import evdev
from evdev import InputDevice, categorize, ecodes
from evdev import UInput, UInputError

events_to_ignore = [ecodes.ABS_Y, ecodes.ABS_X,  ecodes.ABS_RY, ecodes.ABS_RX]
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    print(device.path, device.name, device.phys)
    if device.name == 'xpad' or device.name == 'Generic X-Box pad':
        for event in device.read_loop():
            absevent = categorize(event)
            if absevent.event.code in events_to_ignore:
                continue
            print(ecodes.bytype[absevent.event.type]
                  [absevent.event.code], absevent.event.value)
