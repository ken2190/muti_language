from page.BasePage import BasePage

PACKAGE_NAME = 'com.hanlanguage.hanbook'


class MainPage(BasePage):
    Course = 'Course'
    Dictionary = 'Dictionary'
    Flashcard = 'Flashcard'
    Me = 'Me'


class VIP(BasePage):
    history = 'com.hanlanguage.hanbook:id/ivHistory'
    message = 'com.hanlanguage.hanbook:id/ivMessage'
    collection = 'com.hanlanguage.hanbook:id/ivCollection'
    feedback = 'com.hanlanguage.hanbook:id/ivFeedback'
    setting = 'com.hanlanguage.hanbook:id/ivSetting'
