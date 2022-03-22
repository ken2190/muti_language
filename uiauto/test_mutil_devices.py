from uiauto.device.device import BaseDevice, get_devices_list

if __name__ == '__main__':
    devices = get_devices_list()
    d1=BaseDevice(_d=devices[0])
    d2=BaseDevice(_d=devices[0])
    print("d1"+d1)
    print("d2"+d2)
