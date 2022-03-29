import os
import time
from builtins import print

from uiauto.page.Vpn import V2rayPage


def connect_vpn(device):
    _open_vpn_app(device)
    if device.exits(V2rayPage.CONNECTEDSTATUS):
        print("VPN连接中，不需要连接")
        return
    device.click(V2rayPage.connect)
    if device.exits(V2rayPage.CONNECTEDSTATUS):
        print("VPN连接成功")


def disconnect_vpn(device):
    _open_vpn_app(device)
    if device.exits(V2rayPage.NOCONNECTSTATUS):
        print("VPN已断开，不需要断开")
        return
    device.click(V2rayPage.connect)
    time.sleep(3)
    if device.exits(V2rayPage.NOCONNECTSTATUS):
        print("VPN断开连接")


def _open_vpn_app(device):
    device.app_start(V2rayPage.PACKAGE_NAME)
    device.device.wait_activity(V2rayPage.activity)


def view_allure_report(dir='../report', host='127.0.0.1', port='9999'):
    cmd = 'allure serve ' + dir + ' -h ' + host + ' -p ' + port
    os.system(cmd)


if __name__ == '__main__':
    view_allure_report()
