from time import sleep

from uiautomator2 import Direction

from uiauto.device import Device

if __name__ == '__main__':
    de = Device(debug=1)
    while True:
        de.swip(Direction.LEFT)
        sleep(1.1)


