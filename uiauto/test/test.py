import threading

import pytest

from uiauto.config import devices
from uiauto.device.device import BaseDevice
from uiauto.utils.adb import get_devices_list


@pytest.fixture()
def device():
    b = devices.pop()
    yield BaseDevice()(b)
    devices.append(b)


class TestMy:
    def test_in(self, device):
        d = device
        print(threading.current_thread().name)
        print(d.serial + '___________________________________')


if __name__ == '__main__':
    devices.extend(get_devices_list())
    pytest.main()
