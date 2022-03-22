from uiauto.page.BasePage import BasePage


class CoursePage(BasePage):
    top_Subscribe = 'com.hanlanguage.hanbook:id/tvSubscribe'

    top_pinyin = 'Pinyin Instructions'
    top_stroke = 'Strokes & Radicals'
    top_speakingcard = 'Speaking Practice'
    top_1to1 = '1-on-1    Tutor'

    live_class = 'com.hanlanguage.hanbook:id/ctlFirst'  # todo

    ai_course_list = 'com.hanlanguage.hanbook:id/rvCourse'
    ai_first_course = '//*[@resource-id="com.hanlanguage.hanbook:id/rvCourse"]/android.view.ViewGroup[1]'
    ai_course_title = 'com.hanlanguage.hanbook:id/tvAICourse'


class ClassDetailPage(BasePage):
    activity = '.course.ui.view.CourseClassDetailActivity'

    node_list = 'com.hanlanguage.hanbook:id/rvClass'
    first_node = '//*[@resource-id="com.hanlanguage.hanbook:id/rvClass"]/android.view.ViewGroup[1]'


class VideoPage(BasePage):
    activity = '.study.ui.view.aicourse.InteractiveVideoActivity'

    cotinue_cancel = 'com.hanlanguage.hanbook:id/tvCancel'
    cotinue_yes = 'com.hanlanguage.hanbook:id/tvContinue'

    subtitle = 'com.hanlanguage.hanbook:id/sivSubtitleBtn'
    subtitle_pinyin = 'com.hanlanguage.hanbook:id/tvCheckPY'
    subtitle_english = 'com.hanlanguage.hanbook:id/tvCheckEN'
    speed = 'com.hanlanguage.hanbook:id/tvSpeedBtn'

    video_pause = 'com.hanlanguage.hanbook:id/ivPlayBtn'

    video_close = 'com.hanlanguage.hanbook:id/sivCloseBtn'
    video_close_yes = 'com.hanlanguage.hanbook:id/tvQuit'
    video_close_no = 'com.hanlanguage.hanbook:id/tvContinue'

    continue_button = 'com.hanlanguage.hanbook:id/tvGoQue'


class QuestionPage(BasePage):
    activity = '.study.ui.view.aicourse.InteractiveVideoActivity'

    question_close = 'com.hanlanguage.hanbook:id/ivQueClose'
    question_close_yes = 'com.hanlanguage.hanbook:id/tvQuit'
    question_close_no = 'com.hanlanguage.hanbook:id/tvContinue'

    voice_speed = 'com.hanlanguage.hanbook:id/tvSpeed'

    voice_standard = 'com.hanlanguage.hanbook:id/viewStandardClick'
    voice_read = 'com.hanlanguage.hanbook:id/ivRead'
    voice_myvoice = 'com.hanlanguage.hanbook:id/lavRecord'
    voice_record = 'com.hanlanguage.hanbook:id/tvMyRecord'
    voice_continue = 'com.hanlanguage.hanbook:id/tvContinue'
    voice_skip = 'com.hanlanguage.hanbook:id/tvSkip'

    question_title = 'com.hanlanguage.hanbook:id/tvTitle'
    question_option_list = 'com.hanlanguage.hanbook:id/revOption'
