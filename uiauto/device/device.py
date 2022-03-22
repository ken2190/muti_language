import os

import subprocess

import uiautomator2 as u2

from uiautomator2 import Direction


def get_devices_list():
    cmd = "adb devices"
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()
    out = pr.stdout.readlines()
    devices = []
    for i in out[1:-1]:
        # if str(i).__contains__("."):  # 只获取wifi连接的手机
        device = str(i).split("\\")[0].split("'")[-1]
        #     devices.append(device)     只取wifi连接的
        devices.append(device)
    return devices


def connect_devices(ips_):
    # os.system("adb tcpip 5555")
    if isinstance(ips_, (list, tuple)):
        for ip in ips_:
            os.system("adb connect " + ip)
    elif isinstance(ips_, str):
        os.system("adb connect " + ips_)


def disconnect_device(no):
    # no is serial or wlan_ip
    os.system("adb disconnect " + no)


def install(wlan_ip, package_path):
    cmd = "adb -s" + wlan_ip + " install " + package_path
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out = pr.stdout.readlines()


class BaseDevice:
    _device = None

    @staticmethod
    def _new(_d=None):
        if BaseDevice._device is None:
            print("开始创建设备实例")
            BaseDevice._device = u2.connect(_d)
            # 修改默认配置
            BaseDevice._device.settings['operation_delay'] = (0.5, 1.5)
            BaseDevice._device.settings['operation_delay_methods'] = ['click', 'swipe' 'drag', 'press']
            BaseDevice._device.jsonrpc.setConfigurator({'waitForSelectorTimeout': 10})
            BaseDevice._device.settings['xpath_debug'] = True  # 开启xpath插件的调试日志
            BaseDevice._device.settings['wait_timeout'] = 20.0  # 默认控件等待时间（原生操作，xpath插件的等待时间）

            # 单独线程处理弹窗
            BaseDevice._device.watcher.when(
                '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
            # self.device.watcher.when('//*[@resource-id="android:id/button2"]').click()  # 安装时用的
            # _device.watcher.start()
            # rep = HTMLReport(device, "report/" + str(time()))
            # rep.patch_click()
            print("我创建成功了")

        return BaseDevice._device

    def __init__(self, _d=None, debug=0):
        self.device = BaseDevice._new(_d)
        self.sn = self.device.wlan_ip
        self.brand = str.upper(self.device.device_info.get("brand"))
        if debug == 0:
            self.device.app_stop_all()

    def click(self, element: str):
        self.locate(element).click()

    def click_down_until_exits(self, element: str, direction=Direction.UP, max=3, always=False):
        retry = 0
        if always:
            max = 99
        while not self.exits(element):
            self.swip(direction)
            retry += 1
            if retry > max:
                break
        self.click(element)

    def click_up_until_exits(self, element: str, direction=Direction.DOWN, max=3, always=False):
        retry = 0
        if always:
            max = 99
        while not self.exits(element):
            self.swip(direction)
            retry += 1
            if retry > max:
                break
        self.click(element)

    def app_start(self, package_name):
        self.device.app_start(package_name)

    def locate(self, element: str):
        if element.startswith("com"):
            return self.device(resourceId=element)
        elif element.startswith("//"):
            return self.device.xpath(element)
        elif element.__contains__("."):
            return self.device(className=element)
        else:
            return self.device(text=element)

    def exits(self, element: str):
        return self.locate(element).exists

    def swip(self, direction):
        self.device.swipe_ext(direction)
        self.locate('ss')

    def back(self):
        self.device.press("back")


if __name__ == '__main__':
    pass
