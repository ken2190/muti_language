from concurrent.futures.thread import ThreadPoolExecutor

from uiauto.device.device import BaseDevice
from uiauto.test.test_qudao_package_list import start
from uiauto.utils.adb import get_devices_list
from uiauto.config import devices

package_list = [
    '/app/2022/1.6.3/app-hb_precious-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_nico-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_liuning_dolores-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_lbchanyu-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_india-release_163_jiagu_sign.apk',
]


def test_result(future):
    print(future.result())


def device_pools_init(addresses):
    threadPool = ThreadPoolExecutor(max_workers=len(addresses), thread_name_prefix="device_")
    return threadPool


if __name__ == '__main__':
    devices.extend(get_devices_list())

    test_suite = './test/test_qudao.py'
    device_pools = device_pools_init(devices)
    for package in package_list:
        future = device_pools.submit(start, package, test_suite)
        future.add_done_callback(test_result)
