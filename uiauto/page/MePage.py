from uiauto.page.BasePage import BasePage

PACKAGE_NAME = 'com.hanlanguage.hanbook'


class MePage(BasePage):
    activity = ".main.ui.view.MainActivity"
    top_avatar = 'com.hanlanguage.hanbook:id/sivPortrait'
    top_username = 'com.hanlanguage.hanbook:id/tvUserName'
    top_setting = 'com.hanlanguage.hanbook:id/ivSetting'

    collection = 'com.hanlanguage.hanbook:id/ivCollection'
    history = 'com.hanlanguage.hanbook:id/ivHistory'
    feedback = 'com.hanlanguage.hanbook:id/ivFeedback'
    message = 'com.hanlanguage.hanbook:id/ivMessage'

    course_subscribe = "com.hanlanguage.hanbook:id/tvSubscribeBtn"
    course_subscribed = 'Subscribed by month'
    course_ai = "Comprehensive Course For Beginners"
    course_live = "Kungfu Character"
    course_pinyin = "Pinyin Pronuciation Guide"
    course_speakingcard = "Speaking Practice"
    course_speakingcard_1 = "com.hanlanguage.hanbook:id/sivCard1"
    course_speakingcard_more = "com.hanlanguage.hanbook:id/tvCardMore"

    link_update = 'Update announcement'
    link_1to1 = 'Get 1 on 1 tutor'
    link_invite = 'Invite friends'
    link_facebook = 'Follow us on Facebook'
    link_whatsapp = 'Join Whatsapp group'
    link_playorstore = 'Review on Google Play'


class MyCollectionPage(BasePage):
    activity = ".flash.ui.view.MyCollectActivity"

    edit = "com.hanlanguage.hanbook:id/tvRightEdit"
    list = "com.hanlanguage.hanbook:id/slideRecyclerWords"
    studyInFlash = "com.hanlanguage.hanbook:id/tvStudyInFlash"
    single_delete = "com.hanlanguage.hanbook:id/ctlDelete"
    multi_delete = "com.hanlanguage.hanbook:id/tvSelectedDel"
    cancel = "com.hanlanguage.hanbook:id/tvCancel"
    confirm = "com.hanlanguage.hanbook:id/tvConfirm"
    done = "com.hanlanguage.hanbook:id/tvRightDone"


class HistoryPage(BasePage):
    activity = '.personal.ui.view.HistoryActivity'

    list = 'com.hanlanguage.hanbook:id/recyclerView'

    word = "com.hanlanguage.hanbook:id/ctlWordLayout"
    read = "com.hanlanguage.hanbook:id/imgRead"
    write = "com.hanlanguage.hanbook:id/imgWrite"


class FeedbackListPage(BasePage):
    activity = '.main.ui.view.WebViewActivity'

    list = '//*[@resource-id="com.hanlanguage.hanbook:id/clWebContainer"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'

    back = 'com.hanlanguage.hanbook:id/tvBack'
    faq = 'com.hanlanguage.hanbook:id/tvTitleRight'
    feedback = 'com.hanlanguage.hanbook:id/mbtFeedback'


class MeInformationPage(BasePage):
    activity = '.personal.ui.view.UserProfileActivity'

    portrait = 'com.hanlanguage.hanbook:id/sivPortrait'
    name = 'com.hanlanguage.hanbook:id/clNickName'
    email = 'com.hanlanguage.hanbook:id/clEmail'
    region = 'com.hanlanguage.hanbook:id/clRegion'
    gender = 'com.hanlanguage.hanbook:id/tvGender'
    identity = 'com.hanlanguage.hanbook:id/tvIdentity'
    education = 'com.hanlanguage.hanbook:id/tvEducation'
    purpose = 'com.hanlanguage.hanbook:id/tvPurpose'


class MessagePage(BasePage):
    activity = '.vip.ui.view.MessageActivity'


class SetPage(BasePage):
    activity = '.vip.ui.view.SettingActivity'

    profile = 'com.hanlanguage.hanbook:id/clEditProfile'
    notifiy = 'com.hanlanguage.hanbook:id/tvNotificationTitle'
    notifiy_switch = 'com.hanlanguage.hanbook:id/switchNotification'
    clearcache = 'com.hanlanguage.hanbook:id/tvCacheTitle'
    review_appstore = 'com.hanlanguage.hanbook:id/tvReviewTitle'
    faq = 'com.hanlanguage.hanbook:id/tvQuestionTitle'
    contect = 'com.hanlanguage.hanbook:id/tvAboutTitle'
    logout = 'com.hanlanguage.hanbook:id/mbtExit'
