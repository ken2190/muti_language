from page.BasePage import BasePage


class CourseList(BasePage):
    list = '//*[@resource-id="com.hanlanguage.hanbook:id/recycler"]'
    lock = 'com.hanlanguage.hanbook:id/ivLock'
    bg = 'com.hanlanguage.hanbook:id/sivBg'  # 最新已学
