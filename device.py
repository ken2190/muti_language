import logging
import os

import subprocess
from time import sleep, time

import uiautomator2 as u2

from uiautomator2 import Direction, UiObjectNotFoundError
from uiautomator2.exceptions import XPathElementNotFoundError
from uiautomator2.ext.htmlreport import HTMLReport

import config
import hanbook

SETTING_PACKAGE = "com.android.settings"


def get_devices_list():
    cmd = "adb devices"
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()
    out = pr.stdout.readlines()
    devices = []
    for i in out[1:-1]:
        if str(i).__contains__("."):  # 只获取wifi连接的手机
            device = str(i).split("\\")[0].split("'")[-1]
            devices.append(device)
    return devices


def connect_devices(ips_):
    # os.system("adb tcpip 5555")
    if isinstance(ips_, (list, tuple)):
        for ip in ips_:
            os.system("adb connect " + ip)
    elif isinstance(ips_, str):
        os.system("adb connect " + ips_)


def disconnect_device(wlan_ip):
    os.system("adb disconnect " + wlan_ip)


def install(wlan_ip):
    cmd = "adb -s" + wlan_ip + " install " + config.package_path
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out = pr.stdout.readlines()


class BaseDevice:
    def __init__(self, _d=None, debug=0):
        self.language_list = []
        self.d = u2.connect(_d)
        self.sn = self.d.wlan_ip

        self.brand = str.upper(self.d.device_info.get("brand"))

        # 修改默认配置
        self.d.settings['operation_delay'] = (0.5, 1.5)
        self.d.settings['operation_delay_methods'] = ['click', 'swipe' 'drag', 'press']
        self.d.jsonrpc.setConfigurator({'waitForSelectorTimeout': 5})
        self.d.settings['xpath_debug'] = True  # 开启xpath插件的调试日志
        self.d.settings['wait_timeout'] = 30.0  # 默认控件等待时间（原生操作，xpath插件的等待时间）

        # 单独线程处理弹窗
        self.d.watcher.when(
            '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
        # self.d.watcher.when('//*[@resource-id="android:id/button2"]').click()  # 安装时用的
        self.d.watcher.start()
        if debug == 0:
            self.d.app_stop_all()
        rep = HTMLReport(self.d, "report/" + str(time()))
        rep.patch_click()

    def click(self, element: str):
        self.locate(element).click()

    def locate(self, element: str):
        if element.startswith("com"):
            return self.d(resourceId=element)
        elif element.startswith("//"):
            return self.d.xpath(element)
        else:
            return self.d(text=element)

    def swip_fixed(self):
        self.d.swipe_points([[100, 100], [100, 500]])

    def swip(self, direction):
        self.d.swipe_ext(direction)


class Device(BaseDevice):

    def switch_language(self, language_):
        self.goto_language()
        while not self.d.exists(text=language_):
            self.d.swipe_ext(Direction.FORWARD)
            # sleep(2)
        self.d(text=language_).click()
        if self.d(resourceId="com.android.settings:id/oppo_menu_complete").exists:  # oppo点完成
            self.d(resourceId="com.android.settings:id/oppo_menu_complete").click()
        elif self.d(resourceId="com.android.settings:id/menu_complete").exists:  # realme点完成
            self.d(resourceId="com.android.settings:id/menu_complete").click()
            self.d(resourceId="android:id/button1").click()
            for i in range(6):
                self.d(description="1").click()
        self.d.app_stop(SETTING_PACKAGE)

        # 获取当前设备所有语言

    def get_language_list(self):
        self.goto_language()
        while True:
            li = self.d(resourceId=config.resourceId.get(self.brand)).child(resourceId="android:id/title")
            if self.language_list.__contains__(li[-1].get_text()):
                break
            for i in range(len(li) - 1, -1, -1):
                if not self.language_list.__contains__(li[i].get_text()):
                    self.language_list.append(li[i].get_text())
                else:
                    break
            self.d.swipe_ext(Direction.FORWARD)
            sleep(2)
        self.d.app_stop(SETTING_PACKAGE)

    def goto_language(self):
        import switch_language_func
        func = getattr(self, self.brand)
        MAX_RETRY = 3
        retry = 0
        try:
            func()
        except (UiObjectNotFoundError, XPathElementNotFoundError) as e:
            if retry <= MAX_RETRY:
                retry += 1
                self.d.app_stop(SETTING_PACKAGE)
                logging.warning("开始重试" + str(retry))
                func(self.d)
            else:
                logging.error(self.sn + "实在是定位不了:  " + e)

    def single_test(self):
        self.d.app_start(hanbook.PACKAGE_NAME)

        # 判断是否需要登录
        # if d(resourceId="com.hanlanguage.hanbook:id/tvUName").get_text() == "Sign in":
        #     d(resourceId="com.hanlanguage.hanbook:id/tvUName").click()
        # 切换tab
        hanbook.click(self.d, hanbook.BasePage.mine)
        hanbook.click(self.d, hanbook.BasePage.flashcard)
        hanbook.click(self.d, hanbook.BasePage.dictionary)

        # 查看词条详情
        self.d(resourceId="com.hanlanguage.hanbook:id/tvSearch").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/editContent").send_keys("周")
        self.d.xpath('//*[@resource-id="com.hanlanguage.hanbook:id/recyclerResult"]/android.view.ViewGroup[1]').click()
        assert self.d(resourceId="com.hanlanguage.hanbook:id/tvInitialTitle").get_text() == "Initial:"
        assert self.d(resourceId="com.hanlanguage.hanbook:id/tvVowelTitle").get_text() == "Final(T1):"
        assert self.d(resourceId="com.hanlanguage.hanbook:id/tvRadicalTitle").get_text() == "Radical:"
        assert self.d(resourceId="com.hanlanguage.hanbook:id/tvStrokesTitle").get_text() == "Strokes:"
        assert self.d(resourceId="com.hanlanguage.hanbook:id/tvStructureTitle").get_text() == "Structure:"

        # 切换搜索方式
        self.d(resourceId="com.hanlanguage.hanbook:id/ivBack").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/imgInputVoice").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/imgInputHand").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/imgInputPinyin").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/imgInputRadical").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/imgInputCamera").click()
        self.d(resourceId="com.hanlanguage.hanbook:id/imgClose").click()

    def VIVO(self):
        self.d.app_start("com.android.settings")

        self.d.wait_activity(".MiuiSettings")
        self.d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        self.click('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[11]')
        self.click('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[13]')
        self.click('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]')

    def POCO(self):
        self.d.app_start("com.android.settings")
        self.d.wait_activity(".homepage.SettingsHomepageActivity")
        self.d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        self.d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.widget.ImageView")[
            -1].click()
        self.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]')
        self.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]')

    def XIAOMI(self):
        self.d.app_start("com.android.settings")
        self.d.wait_activity(".homepage.SettingsHomepageActivity")
        self.d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        self.d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.widget.ImageView")[
            -1].click()
        self.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]')
        self.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]')

    def OPPO(self):
        self.d.app_start("com.android.settings")

        self.d.wait_activity("com.oppo.settings.SettingsActivity")
        self.d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        self.click('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[9]')
        self.click('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]')

    def REALME(self):
        self.d.app_start("com.android.settings")

        self.d.wait_activity("com.coloros.settings.feature.homepage.ColorSettingsHomepageActivity")
        sleep(2)
        # d.swipe_ext("up", scale=0.95, steps=3)
        self.d.swipe_ext(Direction.FORWARD)
        sleep(1)
        self.d.swipe_ext(Direction.FORWARD)
        # d.swipe_ext("up", scale=0.95, steps=3)
        sleep(2)
        # d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[9]').click()
        self.d.click(0.276, 0.578)
        self.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[4]')
