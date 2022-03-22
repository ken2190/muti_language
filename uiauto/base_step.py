import logging
import time

from uiautomator2 import Direction, UiObjectNotFoundError
from uiautomator2.exceptions import XPathElementNotFoundError

from uiauto.device.device import BaseDevice
from uiauto.page.BasePage import BasePage
from uiauto.page.MainPage import PACKAGE_NAME, MainPage, BasicInfoPage, update_datail_cancel


def login(device: BaseDevice):
    device.app_start(PACKAGE_NAME)
    if not device.device.wait_activity(BasicInfoPage.activity):
        print('已登录，无需再登录')
        return
    device.device.wait_activity(BasicInfoPage.activity)
    time.sleep(5)
    device.click(BasicInfoPage.first_worker)
    device.click(BasicInfoPage.second_beginner)
    device.click(BasicInfoPage.login_facebook)
    assert device.device.wait_activity(MainPage.activity)
    if device.exits(update_datail_cancel):
        device.click(update_datail_cancel)


SETTING_PACKAGE = "com.androidevice.settings"

screen_lock_password = '111111'

resourceIds = {
    "VIVO": "android:id/list",
    "POCO": "com.android.settings:id/recycler_view",
    "XIAOMI": "com.android.settings:id/recycler_view",
    "OPPO": "android:id/list",
    "REALME": "android:id/list",
}


class SetPage(BasePage):
    oppo_done = "com.androidevice.settings:id/oppo_menu_complete"
    realme_done = "com.androidevice.settings:id/menu_complete"
    realme_done_confirm = "android:id/button1"


def switch_language(language_, device: BaseDevice):
    _goto_language(device)
    device.click_down_until_exits(language_, max=50)
    if device.exits(SetPage.oppo_done):  # oppo点完成
        device.click(SetPage.oppo_done)
    elif device.exits(SetPage.realme_done):  # realme点完成
        device.click(SetPage.realme_done)
        device.click(SetPage.realme_done_confirm)
        for i in screen_lock_password:
            device.click(str(i))
    device.device.app_stop(SETTING_PACKAGE)


def get_language_list(device: BaseDevice):
    language_list = []
    _goto_language()
    while True:
        li = device.locate(resourceIds.get(device.brand)).child(resourceId="android:id/title")
        if device.language_list.__contains__(li[-1].get_text()):
            break
        for i in range(len(li) - 1, -1, -1):
            if not language_list.__contains__(li[i].get_text()):
                language_list.append(li[i].get_text())
            else:
                break
        device.device.swip(Direction.FORWARD)
        time.sleep(2)
    device.device.app_stop(SETTING_PACKAGE)
    return language_list


def _goto_language(device: BaseDevice):
    func = getattr(device.brand)
    MAX_RETRY = 3
    retry = 0
    try:
        func()
    except (UiObjectNotFoundError, XPathElementNotFoundError) as e:
        if retry <= MAX_RETRY:
            retry += 1
            device.device.app_stop(SETTING_PACKAGE)
            logging.warning("开始重试" + str(retry))
            func(device.d)
        else:
            logging.error(device.sn + "实在是定位不了:  " + e)


def VIVO(device: BaseDevice):
    device.device.app_start("com.androidevice.settings")

    device.device.wait_activity(".MiuiSettings")
    device.device.swipe_ext("up", scale=0.95, steps=3)
    time.sleep(1)
    device.click(
        '//*[@resource-id="com.androidevice.settings:id/dashboard_container"]/androidevice.widget.LinearLayout[11]')
    device.click('//*[@resource-id="android:id/list"]/androidevice.widget.LinearLayout[13]')
    device.click('//*[@resource-id="android:id/list"]/androidevice.widget.LinearLayout[1]')


def POCO(device: BaseDevice):
    device.device.app_start("com.androidevice.settings")
    device.device.wait_activity(".homepage.SettingsHomepageActivity")
    device.device.swipe_ext("up", scale=0.95, steps=3)
    time.sleep(1)
    device.locate("androidx.recyclerview.widget.RecyclerView").child(className="androidevice.widget.ImageView")[
        -1].click()
    device.click('//*[@resource-id="com.androidevice.settings:id/recycler_view"]/androidevice.widget.LinearLayout[2]')
    device.click('//*[@resource-id="com.androidevice.settings:id/recycler_view"]/androidevice.widget.LinearLayout[1]')


def XIAOMI(device: BaseDevice):
    device.device.app_start("com.androidevice.settings")
    device.device.wait_activity(".homepage.SettingsHomepageActivity")
    device.device.swipe_ext("up", scale=0.95, steps=3)
    time.sleep(1)
    device.locate("androidx.recyclerview.widget.RecyclerView").child(className="androidevice.widget.ImageView")[
        -1].click()
    device.click('//*[@resource-id="com.androidevice.settings:id/recycler_view"]/androidevice.widget.LinearLayout[2]')
    device.click('//*[@resource-id="com.androidevice.settings:id/recycler_view"]/androidevice.widget.LinearLayout[1]')


def OPPO(device: BaseDevice):
    device.device.app_start("com.androidevice.settings")

    device.device.wait_activity("com.oppo.settings.SettingsActivity")
    device.device.swipe_ext("up", scale=0.95, steps=3)
    time.sleep(1)
    device.click('//*[@resource-id="android:id/list"]/androidevice.widget.LinearLayout[9]')
    device.click('//*[@resource-id="android:id/list"]/androidevice.widget.LinearLayout[2]')


def REALME(device: BaseDevice):
    device.device.app_start("com.androidevice.settings")

    device.device.wait_activity("com.coloros.settings.feature.homepage.ColorSettingsHomepageActivity")
    time.sleep(2)
    # device.swipe_ext("up", scale=0.95, steps=3)
    device.swip(Direction.FORWARD)
    time.sleep(1)
    device.swip(Direction.FORWARD)
    # device.swipe_ext("up", scale=0.95, steps=3)
    time.sleep(2)
    # device.xpath('//*[@resource-id="com.androidevice.settings:id/recycler_view"]/androidevice.widget.LinearLayout[9]').click()
    device.device.click(0.276, 0.578)
    device.click('//*[@resource-id="com.androidevice.settings:id/recycler_view"]/androidevice.widget.LinearLayout[4]')
