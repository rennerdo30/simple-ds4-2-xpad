#!/usr/bin/python3

import evdev
from evdev import InputDevice, categorize, ecodes
from evdev import UInput, UInputError

XBOX_BUTTON_TRIANGLE = 308
XBOX_BUTTON_O = 305
XBOX_BUTTON_X = 304
XBOX_BUTTON_RECTANGLE = 307

XBOX_BUTTON_SHARE = 314
XBOX_BUTTON_OPTIONS = 315

XBOX_BUTTON_PLAYSTATION = 316

XBOX_BUTTON_R1 = 311
XBOX_BUTTON_R2 = 313  # does not work??
XBOX_BUTTON_L1 = 310
XBOX_BUTTON_L2 = 312  # does not work??

XBOX_BUTTON_LS = 317
XBOX_BUTTON_RS = 318


DS4_BUTTON_TRIANGLE = 307
DS4_BUTTON_O = 305
DS4_BUTTON_X = 304
DS4_BUTTON_RECTANGLE = 308

DS4_BUTTON_SHARE = 314
DS4_BUTTON_OPTIONS = 315

DS4_BUTTON_PLAYSTATION = 316

DS4_BUTTON_R1 = 311
DS4_BUTTON_R2 = 313
DS4_BUTTON_L1 = 310
DS4_BUTTON_L2 = 312

DS4_BUTTON_LS = 317
DS4_BUTTON_RS = 318

DS4_NAMES = [ 'Sony Interactive Entertainment Wireless Controller', 'Sony Computer Entertainment Wireless Controller' ]

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)


def create_device():
    events = {ecodes.EV_ABS: [], ecodes.EV_KEY: [], ecodes.EV_REL: []}

    events[ecodes.EV_ABS].append((ecodes.ABS_X, {}))
    events[ecodes.EV_ABS].append((ecodes.ABS_Y, {}))
    events[ecodes.EV_ABS].append((ecodes.ABS_RX, {}))
    events[ecodes.EV_ABS].append((ecodes.ABS_RY, {}))
    events[ecodes.EV_ABS].append((ecodes.ABS_Z, {}))
    events[ecodes.EV_ABS].append((ecodes.ABS_RZ, {}))

    events[ecodes.EV_ABS].append((ecodes.ABS_HAT0X, {}))
    events[ecodes.EV_ABS].append((ecodes.ABS_HAT0Y, {}))

    events[ecodes.EV_KEY].append(ecodes.BTN_START)
    events[ecodes.EV_KEY].append(ecodes.BTN_MODE)
    events[ecodes.EV_KEY].append(ecodes.BTN_SELECT)
    events[ecodes.EV_KEY].append(ecodes.BTN_A)
    events[ecodes.EV_KEY].append(ecodes.BTN_B)
    events[ecodes.EV_KEY].append(ecodes.BTN_X)
    events[ecodes.EV_KEY].append(ecodes.BTN_Y)
    events[ecodes.EV_KEY].append(ecodes.BTN_TL)
    events[ecodes.EV_KEY].append(ecodes.BTN_TR)
    events[ecodes.EV_KEY].append(ecodes.BTN_THUMBL)
    events[ecodes.EV_KEY].append(ecodes.BTN_THUMBR)
    device = UInput(name="xpad", events=events,
                    bustype=ecodes.BUS_USB, vendor=1118, product=654, version=272)
    return device


devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
ds4 = None
for device in devices:
    print(device.path, device.name, device.phys)
    if device.name in DS4_NAMES:
        print("Found DS4")
        ds4 = device
        break

if ds4 is not None:
    xbox_controller = create_device()
    for event in ds4.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.code == DS4_BUTTON_TRIANGLE:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_TRIANGLE, event.value)
            elif event.code == DS4_BUTTON_O:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_O, event.value)
            elif event.code == DS4_BUTTON_X:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_X, event.value)
            elif event.code == DS4_BUTTON_RECTANGLE:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_RECTANGLE, event.value)
            elif event.code == DS4_BUTTON_SHARE:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_SHARE, event.value)
            elif event.code == DS4_BUTTON_OPTIONS:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_OPTIONS, event.value)
            elif event.code == DS4_BUTTON_PLAYSTATION:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_PLAYSTATION, event.value)
            elif event.code == DS4_BUTTON_R1:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_R1, event.value)
            elif event.code == DS4_BUTTON_R2:
                continue
            elif event.code == DS4_BUTTON_L1:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_L1, event.value)
            elif event.code == DS4_BUTTON_L2:
                continue
            elif event.code == DS4_BUTTON_LS:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_LS, event.value)
            elif event.code == DS4_BUTTON_RS:
                xbox_controller.write(
                    ecodes.EV_KEY, XBOX_BUTTON_RS, event.value)
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)

            if absevent.event.code == ecodes.ABS_Y or absevent.event.code == ecodes.ABS_X or absevent.event.code == ecodes.ABS_RY or absevent.event.code == ecodes.ABS_RX:
                value = int(translate(absevent.event.value, 0, 255, -32768, 32767))
                xbox_controller.write(
                    ecodes.EV_ABS, absevent.event.code, value)
            elif absevent.event.code == ecodes.ABS_Z:
                value = int(translate(absevent.event.value, 0, 255, -32768, 32767))
                xbox_controller.write(
                    ecodes.EV_ABS, absevent.event.code, value)
            elif absevent.event.code == ecodes.ABS_RZ:
                value = int(translate(absevent.event.value, 0, 255, -32768, 32767))
                xbox_controller.write(
                    ecodes.EV_ABS, absevent.event.code, value)
            else:
                xbox_controller.write(
                    ecodes.EV_ABS, absevent.event.code, absevent.event.value)

        xbox_controller.syn()
