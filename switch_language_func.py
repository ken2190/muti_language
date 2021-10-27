from time import sleep


class func():
    def VIVO(self, d):
        d.app_start("com.android.settings")
        d.wait_activity(".MiuiSettings")
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d.xpath(
            '//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[11]').click()
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[13]').click()
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()

    def POCO(self, d):
        # todo
        d.app_start("com.android.settings")
        d.wait_activity(".homepage.SettingsHomepageActivity")
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d(className="androidx.recyclerview.widget.RecyclerView").child(className="android.widget.ImageView")[
            -1].click()
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]').click()
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]').click()

    def OPPO(self, d):
        d.app_start("com.android.settings")

        d.wait_activity("com.oppo.settings.SettingsActivity")
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[9]').click()
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]').click()

    def REALME(self, d):
        d.app_start("com.android.settings")

        d.wait_activity("com.coloros.settings.feature.homepage.ColorSettingsHomepageActivity")
        sleep(2)
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(1)
        d.swipe_ext("up", scale=0.95, steps=3)
        sleep(2)
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[10]').click()
        d.xpath('//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[4]').click()
