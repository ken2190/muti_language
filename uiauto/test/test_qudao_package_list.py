import uiauto.utils.cmd as cmd
import uiauto.utils.adb as adb
import uiauto.utils.util as util
from uiauto.base_step import login
import unittest

from BeautifulReport import BeautifulReport as bf


def start(package, devices: list):
    path = 'D:/AWork/install/1.6.4/'
    device = devices.pop()
    file = package.split('/')[-1]
    # 下载渠道包
    cmd.download(url=package, save_path=path + file)
    # 卸载并安装新包
    adb.uninstall('com.hanlanguage.hanbook', device)

    adb.install(file=file, serial=device, path=path, replace_old=True)

    # 打开Vpn
    util.connect_vpn(device)

    # 登录用户
    login(device)

    util.disconnect_vpn(device)

    # 开始测试
    runner(file)
    devices.append(device)


def runner(name=''):
    suite = unittest.TestSuite()

    # 指定识别测试用例的规则
    tests = unittest.defaultTestLoader.discover('../test', pattern='test_qudao.py')
    # 识别所有test开头的py文件为测试用例
    # 按模块名顺序执行

    suite.addTest(tests)

    run = bf(suite)  # 实例化BeautifulReport模块
    run.report(filename=name, report_dir='../report/', description='test_qudao_{}'.format(name))
