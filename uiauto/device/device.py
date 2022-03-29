import uiautomator2 as u2

from uiautomator2 import Direction

print("开始Basedevice")


class BaseDevice(object):

    def __init__(self, _d=None):
        print("init")

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

    def back(self):
        self.device.press("back")

    def __call__(self, *args, **kwargs):
        print("call")

        self.device = u2.connect(args[0])
        # 修改默认配置
        self.device.settings['operation_delay'] = (0.5, 1.5)
        self.device.settings['operation_delay_methods'] = ['click', 'swipe' 'drag', 'press']
        self.device.jsonrpc.setConfigurator({'waitForSelectorTimeout': 10})
        self.device.settings['xpath_debug'] = True  # 开启xpath插件的调试日志
        self.device.settings['wait_timeout'] = 20.0  # 默认控件等待时间（原生操作，xpath插件的等待时间）

        # 单独线程处理弹窗
        self.device.watcher.when(
            '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
        # self.device.watcher.when('//*[@resource-id="android:id/button2"]').click()  # 安装时用的
        # _device.watcher.start()
        # rep = HTMLReport(device, "report/" + str(time()))
        # rep.patch_click()
        print("我创建成功了")

        self.sn = self.device.wlan_ip
        self.serial = self.device.serial
        self.brand = str.upper(self.device.device_info.get("brand"))
        return self


print("结束Basedevice")
