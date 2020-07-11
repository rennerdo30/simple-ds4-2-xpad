#!/usr/bin/python3

import evdev
from evdev import InputDevice, categorize, ecodes
from evdev import UInput, UInputError


devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    print(device.path, device.name, device.phys)
