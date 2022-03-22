from uiauto.page.BasePage import BasePage

PACKAGE_NAME = 'com.hanlanguage.hanbook'


class DictionaryPage(BasePage):
    activity = ".main.ui.view.MainActivity"

    search_box = "com.hanlanguage.hanbook:id/tvSearch"
    search_speech = "com.hanlanguage.hanbook:id/ivTagSpeech"
    search_write = "com.hanlanguage.hanbook:id/ivTagWriter"
    search_camera = "com.hanlanguage.hanbook:id/ivTagCamera"
    search_pinyin = "com.hanlanguage.hanbook:id/ivTagPinyin"
    search_radicals = "com.hanlanguage.hanbook:id/ivTagRadicals"

    daily_previous = "com.hanlanguage.hanbook:id/tvMore"
    daily_read = "com.hanlanguage.hanbook:id/sivReadBg"
    daily_write = "com.hanlanguage.hanbook:id/sivWriteBg"
    daily_quiz = "com.hanlanguage.hanbook:id/sivQuizBg"

    wordbook_my = '//*[@resource-id="com.hanlanguage.hanbook:id/clContainer"]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]'
    wordbook_recommend = '//*[@resource-id="com.hanlanguage.hanbook:id/clContainer"]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[2]'

    course_subscribe = "Subscribe"
    course_ai = "Comprehensive Course For Beginners"
    course_live = "Kungfu Character"
    course_pinyin = "Pinyin Pronuciation Guide"
    course_speakingcard = "Speaking Practice"
    course_speakingcard_1 = "com.hanlanguage.hanbook:id/sivCard1"
    course_speakingcard_more = "com.hanlanguage.hanbook:id/tvCardMore"

    game_1 = '//*[@resource-id="com.hanlanguage.hanbook:id/refreshLayout"]/androidx.recyclerview.widget.RecyclerView' \
             '[1]/android.view.ViewGroup[4]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]'
    game_2 = '//*[@resource-id="com.hanlanguage.hanbook:id/refreshLayout"]/androidx.recyclerview.widget.RecyclerView' \
             '[1]/android.view.ViewGroup[4]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[2]'
    game_3 = '//*[@resource-id="com.hanlanguage.hanbook:id/refreshLayout"]/androidx.recyclerview.widget.RecyclerView' \
             '[1]/android.view.ViewGroup[4]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[3]'


class DailyPrevious(BasePage):
    activity = '.home.ui.view.activity.PracticeHistoryActivity'

    read = 'com.hanlanguage.hanbook:id/tvReadTag'
    write = 'com.hanlanguage.hanbook:id/tvWriteTag'
    quiz = 'com.hanlanguage.hanbook:id/tvQuizTag'


class SearchPage(BasePage):
    activity = '.search.ui.view.SearchActivity'

    content = 'com.hanlanguage.hanbook:id/editContent'
    result_list = 'com.hanlanguage.hanbook:id/recyclerResult'
    clear = 'com.hanlanguage.hanbook:id/imgDelete'
    speech_record = 'com.hanlanguage.hanbook:id/imgVoiceRecord'
    write_eraser = 'com.hanlanguage.hanbook:id/imgHandEraser'
    done = 'com.hanlanguage.hanbook:id/tvBottomDone'


class CameraPage(BasePage):
    activity = '.search.ui.view.TakePhotoActivity'

    take_photo = 'com.hanlanguage.hanbook:id/imgTakePhoto'

    choose = 'com.hanlanguage.hanbook:id/imgPhotoChoose'


class WordsDetailPage(BasePage):
    activity = '.dictionary.ui.view.DictActivity'

    letter_pinyin_list = 'com.hanlanguage.hanbook:id/rvPinyin'

    read = 'com.hanlanguage.hanbook:id/ivReadBg'
    write = 'com.hanlanguage.hanbook:id/ivWriteBg'
    quiz = 'com.hanlanguage.hanbook:id/ivQuizBg'

    dict_show = 'com.hanlanguage.hanbook:id/clAction'

    collection = 'com.hanlanguage.hanbook:id/ivCollection'
    # todo
