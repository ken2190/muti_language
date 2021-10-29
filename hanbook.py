class BasePage(object):
    pass


class Login(BasePage):
    wechat = 'resourceId="com.hanlanguage.hanbook:id/sivWechatWrapper"'
    facebook = 'resourceId="com.hanlanguage.hanbook:id/sivFacebookWrapper"'
    google = 'resourceId="com.hanlanguage.hanbook:id/sivGoogleWrapper"'
    check = 'resourceId="com.hanlanguage.hanbook:id/ivCheck"'
