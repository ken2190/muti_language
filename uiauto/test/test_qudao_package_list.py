import os
import threading
import time

import pytest

from uiauto.base_step import login

from uiauto.utils import mycmd, adb, util


def start(package, test_suite):
    path = 'D:/AWork/install/1.6.4/'
    file = package.split('/')[-1]
    # # 下载渠道包
    # cmd.download(url=package, save_path=path + file)
    # # 卸载并安装新包
    # adb.uninstall('com.hanlanguage.hanbook', d)
    #
    # adb.install(file=file, device=d, path=path, replace_old=True, allow_test=True)
    #
    # # 打开Vpn
    # util.connect_vpn(d)
    #
    # # 登录用户
    # login(d)
    #
    # util.disconnect_vpn(d)

    # 开始测试[
    print(threading.current_thread().name + "开始执行用例")

    runner(test_suite, file + str(time.time()))

    print(threading.current_thread().name + "结束执行用例")


def runner(pattern, name=''):
    pytest.main([pattern, '-k', 'test_feedback', '--alluredir', './report', '--reruns' '3' '--reruns-delay' '2'])
