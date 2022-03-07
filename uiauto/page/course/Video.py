from uiauto.page.BasePage import BasePage


class Video(BasePage):
    activity = '.study.ui.view.aicourse.InteractiveVideoActivity'

    NO = 'No'
    Yes = 'Yes'
    tvPosition = 'com.hanlanguage.hanbook:id/tvPosition'
    tvDuration = 'com.hanlanguage.hanbook:id/tvDuration'
    sivCloseBtn = 'com.hanlanguage.hanbook:id/sivCloseBtn'
    sivSubtitleBtn = 'com.hanlanguage.hanbook:id/sivSubtitleBtn'
    tvSpeedBtn = 'com.hanlanguage.hanbook:id/tvSpeedBtn'
    ivPlayBtn = 'com.hanlanguage.hanbook:id/ivPlayBtn'
    tvInteractiveTitle = 'com.hanlanguage.hanbook:id/tvInteractiveTitle'
    tvInteractiveMore = 'com.hanlanguage.hanbook:id/tvInteractiveMore'
    tvGoQue = 'com.hanlanguage.hanbook:id/tvGoQue'

class Question(BasePage):
    activity = '.study.ui.view.aicourse.InteractiveVideoActivity'
    type = ''

    tvTrans = 'com.hanlanguage.hanbook:id/tvTrans'

    viewStandardClick = 'com.hanlanguage.hanbook:id/viewStandardClick'
    ivRead = 'com.hanlanguage.hanbook:id/ivRead'
    lavRecord = 'com.hanlanguage.hanbook:id/lavRecord'
    ctlAnalysis = 'com.hanlanguage.hanbook:id/ctlAnalysis'
