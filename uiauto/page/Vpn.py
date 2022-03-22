from uiauto.page.BasePage import BasePage


class V2rayPage(BasePage):
    PACKAGE_NAME = 'com.v2ray.ang'
    activity = '.ui.MainActivity'

    NOCONNECTSTATUS = "未连接"
    CONNECTEDSTATUS = "已连接，点击测试连接"
    connect = 'com.v2ray.ang:id/fab'
