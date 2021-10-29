from time import sleep

from uiautomator2 import Direction

from device import Device


def VIVO(de: Device):
    d = de.d
    d.app_start("com.android.settings")

    d.wait_activity(".MiuiSettings")
    d.swipe_ext("up", scale=0.95, steps=3)
    sleep(1)
    de.click('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[11]')
    de.click('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[13]')
    de.click('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]')


def POCO(de: Device):
    d = de.d
    d.app_start("com.android.settings")
    d.wait_activity(".homepage.SettingsHomepageActivity")
    d.swipe_ext("up", scale=0.95, steps=3)
    sleep(1)
    d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.widget.ImageView")[
        -1].click()
    de.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]')
    de.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]')


def XIAOMI(de: Device):
    d = de.d
    d.app_start("com.android.settings")
    d.wait_activity(".homepage.SettingsHomepageActivity")
    d.swipe_ext("up", scale=0.95, steps=3)
    sleep(1)
    d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.widget.ImageView")[
        -1].click()
    de.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]')
    de.click('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]')


def OPPO(d):
    d.app_start("com.android.settings")

    d.wait_activity("com.oppo.settings.SettingsActivity")
    d.swipe_ext("up", scale=0.95, steps=3)
    sleep(1)
    d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[9]').click()
    d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]').click()


def REALME(d: Device):
    d.app_start("com.android.settings")

    d.wait_activity("com.coloros.settings.feature.homepage.ColorSettingsHomepageActivity")
    sleep(2)
    # d.swipe_ext("up", scale=0.95, steps=3)
    d.swipe_ext(Direction.FORWARD)
    sleep(1)
    d.swipe_ext(Direction.FORWARD)
    # d.swipe_ext("up", scale=0.95, steps=3)
    sleep(2)
    # d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[9]').click()
    d.click(0.276, 0.578)
    d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[4]').click()
