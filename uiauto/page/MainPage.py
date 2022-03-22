from uiauto.page.BasePage import BasePage

PACKAGE_NAME = 'com.hanlanguage.hanbook'

update_datail = 'com.hanlanguage.hanbook:id/tvLearn'
update_datail_cancel = 'com.hanlanguage.hanbook:id/ivClose'


class MainPage(BasePage):
    activity = '.main.ui.view.MainActivity'
    Course = 'Course'
    Dictionary = 'Dictionary'
    # Flashcard = 'Flashcard'
    Me = 'Me'


class BasicInfoPage(BasePage):
    activity = '.main.ui.view.BasicInfoActivity'

    first_primary = 'Primary school student'
    first_college = 'College student'
    first_middle_school = 'Middle school student'
    first_worker = 'Staff and worker'
    first_others = 'Others'

    second_beginner = 'Beginner'
    second_elementary = 'Elementary'
    second_pre_intermediate = 'Pre-intermediate'
    second_beginner = 'Intermediate'
    second_upper_intermediate = 'Upper-intermediate'
    second_advanced = 'Advanced'

    login_google = 'com.hanlanguage.hanbook:id/sivGoogleWrapper'
    login_facebook = 'com.hanlanguage.hanbook:id/sivFacebookWrapper'
    login_wechat = 'com.hanlanguage.hanbook:id/sivWechatWrapper'
