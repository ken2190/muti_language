PACKAGE_NAME = 'com.hanlanguage.hanbook'


class BasePage(object):
    dictionary = 'com.hanlanguage.hanbook:id/tabHome'
    flashcard = 'com.hanlanguage.hanbook:id/tabFlash'
    mine = 'com.hanlanguage.hanbook:id/tabVip'
    pass


class Login(BasePage):
    wechat = 'com.hanlanguage.hanbook:id/sivWechatWrapper'
    facebook = 'com.hanlanguage.hanbook:id/sivFacebookWrapper'
    google = 'com.hanlanguage.hanbook:id/sivGoogleWrapper'
    check = 'com.hanlanguage.hanbook:id/ivCheck'


class VIP(BasePage):
    history = 'com.hanlanguage.hanbook:id/ivHistory'
    message = 'com.hanlanguage.hanbook:id/ivMessage'
    collection = 'com.hanlanguage.hanbook:id/ivCollection'
    feedback = 'com.hanlanguage.hanbook:id/ivFeedback'
    setting = 'com.hanlanguage.hanbook:id/ivSetting'


class Hanbook():
    def __init__(self, _d):
        self.d = _d

    def login(self, login_type):
        self.d.click(Login.check)
        self.d.click(Login.check)
        self.d.click(Login.__getattribute__(login_type))
