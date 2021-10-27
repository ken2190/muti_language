import multiprocessing as np
import os

import uiautomator2 as u2
import subprocess
from time import sleep

from uiautomator2 import Direction

import config

d = None
try:
    d = u2.connect("80b914b7")
except RuntimeError as e:
    os.system("adb connect 80b914b7")
d.settings['operation_delay'] = (1, 0.5)

# 修改延迟生效的方法
# 其中 double_click, long_click 都对应click
d.settings['operation_delay_methods'] = ['click', 'swipe' 'drag', 'press']

d.settings['xpath_debug'] = True  # 开启xpath插件的调试日志
d.settings['wait_timeout'] = 20.0  # 默认控件等待时间（原生操作，xpath插件的等待时间）
d.watcher.when(
    '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
d.watcher.when('//*[@resource-id="android:id/button2"]').click()  # 安装时用的

d.watcher.start()

brand = str.upper(d.device_info.get("brand"))
d.app_stop_all()

d.jsonrpc.setConfigurator({'waitForSelectorTimeout': 5})
language_list = []

resourceId = {
    "VIVO": "android:id/list",
    "POCO": "com.android.settings:id/recycler_view",
    "XIAOMI": "com.android.settings:id/recycler_view",
    "OPPO": "android:id/list",
    "OPPO": "android:id/list",
    "REALME": "android:id/list",
}


def run():
    d.app_start("com.hanlanguage.hanbook")
    d(resourceId="com.hanlanguage.hanbook:id/tabVip").click()
    # 判断是否需要登录
    # if d(resourceId="com.hanlanguage.hanbook:id/tvUName").get_text() == "Sign in":
    #     d(resourceId="com.hanlanguage.hanbook:id/tvUName").click()

    d(resourceId="com.hanlanguage.hanbook:id/tabFlash").click()
    d(resourceId="com.hanlanguage.hanbook:id/tabHome").click()
    d(resourceId="com.hanlanguage.hanbook:id/tvSearch").click()
    d(resourceId="com.hanlanguage.hanbook:id/editContent").send_keys("周")
    d.xpath('//*[@resource-id="com.hanlanguage.hanbook:id/recyclerResult"]/android.view.ViewGroup[1]').click()
    try:
        assert d(resourceId="com.hanlanguage.hanbook:id/tvInitialTitle").get_text() == "Initial:"
        assert d(resourceId="com.hanlanguage.hanbook:id/tvVowelTitle").get_text() == "Final(T1):"
        assert d(resourceId="com.hanlanguage.hanbook:id/tvRadicalTitle").get_text() == "Radical:"
        assert d(resourceId="com.hanlanguage.hanbook:id/tvStrokesTitle").get_text() == "Strokes:"
        assert d(resourceId="com.hanlanguage.hanbook:id/tvStructureTitle").get_text() == "Structure:"
    except ValueError:
        print("d.device_info")
    d(resourceId="com.hanlanguage.hanbook:id/ivBack").click()
    d(resourceId="com.hanlanguage.hanbook:id/imgInputVoice").click()
    d(resourceId="com.hanlanguage.hanbook:id/imgInputHand").click()
    d(resourceId="com.hanlanguage.hanbook:id/imgInputPinyin").click()
    d(resourceId="com.hanlanguage.hanbook:id/imgInputRadical").click()

    d(resourceId="com.hanlanguage.hanbook:id/imgInputCamera").click()
    d(resourceId="com.hanlanguage.hanbook:id/imgClose").click()
    d.app_stop("com.hanlanguage.hanbook")


def switch_language(language_):
    goto_language()
    while not d.exists(text=language_):
        d.swipe_ext(Direction.FORWARD)
        # sleep(2)
    d(text=language_).click()
    if d(resourceId="com.android.settings:id/oppo_menu_complete").exists:  # oppo点完成
        d(resourceId="com.android.settings:id/oppo_menu_complete").click()
    elif d(resourceId="com.android.settings:id/menu_complete").exists:  # realme点完成
        d(resourceId="com.android.settings:id/menu_complete").click()
    d.app_stop("com.android.settings")


def get_language_list():
    goto_language()
    while True:
        li = d(resourceId=resourceId.get(brand)).child(resourceId="android:id/title")
        if language_list.__contains__(li[-1].get_text()):
            break
        for i in range(len(li) - 1, -1, -1):
            if not language_list.__contains__(li[i].get_text()):
                language_list.append(li[i].get_text())
            else:
                break
        d.swipe_ext(Direction.FORWARD)
        # sleep(2)
    d.app_stop("com.android.settings")
    return language_list


def goto_language():
    d.app_start("com.android.settings")
    if brand == "VIVO":
        d.wait_activity(".MiuiSettings")
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d.xpath(
            '//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[11]').click()
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[13]').click()
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
    elif brand == "POCO":
        d.wait_activity(".homepage.SettingsHomepageActivity")
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.widget.ImageView")[
            -1].click()
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]').click()
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]').click()
    elif brand == "OPPO":
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[9]').click()
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]').click()
    elif brand == "REALME":
        d.swipe_ext("up", scale=0.95, steps=3)
        d.swipe_ext("up", scale=0.95, steps=3)
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[9]').click()
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[4]').click()


if __name__ == '__main__':
    ips = config.ips
    language_list = get_language_list()
    while language_list:
        language_ = language_list.pop()
        switch_language(language_)
        # run()
        print("执行了" + brand + language_)
