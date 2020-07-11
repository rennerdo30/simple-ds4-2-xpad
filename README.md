# simple-ds4-2-xpad
remapping software from ds4 to xpad

The script must run to remap the inputs. A later release will maybe feature a background service. But for now you need to run it by yourself. 
If this is too much work for you, you could write a systemd unit. The problem with this would be, that the script expects a ds4 to be present.

This script was tested with GTA5 using proton. It ran fine and had no problems, not like other software promising the same.
One major downside of this script is, that is does not offer any special features for the ds4 controller.
It just remaps your buttons and fixes some ranges.

## Installtion
Just download `remapper.py`, install `python-evdev` and run it with `python remapper.py`
