from uiauto.page.BasePage import BasePage


class ExpressionsPage(BasePage):
    activity = '.flash.ui.view.FlashMainActivity'

    tab_name = 'com.hanlanguage.hanbook:id/tvSpeakingCards'  # tab名

    not_finished_continue = 'com.hanlanguage.hanbook:id/tvSpeakCardStudy'
    recommend_filter = 'com.hanlanguage.hanbook:id/topicLayer'
    recommend_list = 'com.hanlanguage.hanbook:id/recyclerTopics'  # 推荐列表


class SpeakingCardGuidePage(BasePage):
    activity = '.study.ui.view.speakcard.SpeakingGuideActivity'

    title = 'com.hanlanguage.hanbook:id/tvCenterTitle'

    review = 'com.hanlanguage.hanbook:id/tvReview'
    continue_button = 'com.hanlanguage.hanbook:id/tvContinueLearn'
    study_again = 'com.hanlanguage.hanbook:id/tvStudyAgain'


class ExpressionsCardPage(BasePage):
    activity = '.study.ui.view.speakcard.SpeakingCardActivity'

    pause = 'com.hanlanguage.hanbook:id/ivPause'
    pause_continue = 'com.hanlanguage.hanbook:id/tvContinue'
    pause_exit = 'com.hanlanguage.hanbook:id/tvExit'

    standard = 'com.hanlanguage.hanbook:id/lavStandard'
    speak = 'com.hanlanguage.hanbook:id/ivSpeak'
    speed = 'com.hanlanguage.hanbook:id/tvSpeed'
    pinyin_hide = 'com.hanlanguage.hanbook:id/ivPyState'

    # result_  todo
