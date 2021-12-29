from time import sleep

from uiautomator2 import Direction

from device import Device

if __name__ == '__main__':
    de = Device(debug=1)
    de.swip(Direction.LEFT)
    sleep(1.1)
