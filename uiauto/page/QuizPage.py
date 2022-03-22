from uiauto.page.BasePage import BasePage


class QuizPage(BasePage):
    activity = ".home.ui.view.activity.PracticeHistoryActivity"

    quiz_list = 'com.hanlanguage.hanbook:id/rvContainer'

    read = 'com.hanlanguage.hanbook:id/tvReadTag'
    read = 'com.hanlanguage.hanbook:id/tvWriteTag'
    quiz = 'com.hanlanguage.hanbook:id/tvQuizTag'
