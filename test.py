import logging
import unittest

import multiprocessing as np

import adbutils

from uiautomator2 import Direction, UiObjectNotFoundError
from uiautomator2.exceptions import XPathElementNotFoundError

import config
import hanbook
from device import connect_devices, disconnect_device, Device


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


def create_test(serial):
    def testhanbook2(self):
        de = Device(serial)

        # 执行用例
        # self.get_language_list()
        de.language_list = config.REALME_LANGUAGE_LIST
        logging.info(de.brand + "_LANGUAGE_LIST=" + str(de.language_list) + "\n")

        while de.language_list:
            language_ = de.language_list.pop()
            de.switch_language(language_)
            try:
                de.single_test()
            except (UiObjectNotFoundError, XPathElementNotFoundError) as e:
                logging.error(de.brand + language_ + "执行失败" + str(e))
            finally:
                logging.info("执行完了" + de.brand + language_)
        de.app_stop(hanbook.PACKAGE_NAME)
        disconnect_device(serial)

    setattr(MyTest, "test" + serial, testhanbook2)
    unittest.main()



if __name__ == '__main__':
    ips = config.ips
    connect_devices(ips)
    li = adbutils.adb.device_list()

    for i in li:
        if i.serial.__contains__("."):  # 只获取wifi连接的手机
            p = np.Process(target=create_test, args=(i.serial,))
            p.run()
