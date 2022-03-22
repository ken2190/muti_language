from concurrent.futures.thread import ThreadPoolExecutor

from uiauto.device import device
from uiauto.test.test_qudao_package_list import start

package_list = [
    '/app/2022/1.6.3/app-hb_precious-release_163_jiagu_sign.apk',
    '/app/2022/1.6.3/app-hb_nico-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_liuning_dolores-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_lbchanyu-release_163_jiagu_sign.apk',
    # '/app/2022/1.6.3/app-hb_india-release_163_jiagu_sign.apk',
]


def test_result(future):
    print(future.result())


def device_pools(packages, addresses):
    threadPool = ThreadPoolExecutor(max_workers=len(addresses), thread_name_prefix="device_")
    for package in packages:
        future = threadPool.submit(start, package, addresses)
        future.add_done_callback(test_result)


if __name__ == '__main__':
    devices = device.get_devices_list()
    device_pools(package_list)
