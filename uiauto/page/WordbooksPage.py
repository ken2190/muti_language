from uiauto.page.BasePage import BasePage


class MyWordbookPage(BasePage):
    activity = '.flash.ui.view.FlashMainActivity'

    tab_name = 'com.hanlanguage.hanbook:id/tvWordBooks'  # tab名

    ongoing_study = 'com.hanlanguage.hanbook:id/tvContinue'
    ongoing_review = 'com.hanlanguage.hanbook:id/tvReview'
    ongoing_allwords = 'com.hanlanguage.hanbook:id/tvAllWords'
    ongoing_title = 'com.hanlanguage.hanbook:id/tvStudyTitle'
    ongoing_book_name = 'com.hanlanguage.hanbook:id/tvBookTitle'
    ongoing_process = 'com.hanlanguage.hanbook:id/tvProcess'  # 进度百分比
    ongoing_notLearnNum = 'com.hanlanguage.hanbook:id/tvNotLearnNum'
    ongoing_reviewNum = 'com.hanlanguage.hanbook:id/tvReviewNum'
    ongoing_studyAgain = 'com.hanlanguage.hanbook:id/tvStudyAgain'

    mywordbook_edit = 'com.hanlanguage.hanbook:id/tvEdit'
    mywordbook_book_list = 'com.hanlanguage.hanbook:id/revWordBooks'
    mywordbook_book_cover = 'com.hanlanguage.hanbook:id/ctlBookMsg'
    mywordbook_add = 'com.hanlanguage.hanbook:id/ctlAdd'
    mywordbook_done = 'com.hanlanguage.hanbook:id/tvDone'
    mywordbook_delete = 'com.hanlanguage.hanbook:id/imgBookDel'
    mywordbook_delete_yes = 'com.hanlanguage.hanbook:id/tvConfirm'
    mywordbook_delete_no = 'com.hanlanguage.hanbook:id/tvCancel'

    popular_title = 'com.hanlanguage.hanbook:id/tvTitle'  # 推荐名称
    popular_recommend = 'com.hanlanguage.hanbook:id/revRecommend'  # 推荐列表
    # todo


# / empty


class AddWordbookPage(BasePage):
    activity = '.flash.ui.view.BookShelfActivity'  #

    tvCenterTitle = 'com.hanlanguage.hanbook:id/tvCenterTitle'

    textbooks = 'com.hanlanguage.hanbook:id/ctlTextbooks'
    industries = 'com.hanlanguage.hanbook:id/ctlIndustries'
    subjects = 'com.hanlanguage.hanbook:id/ctlSubjects'
    list = 'com.hanlanguage.hanbook:id/recyclerView'  # 专集列表

    unfold = 'Unfold'  # 展开收起
    fold = 'fold'  # 展开收起
    book_list = 'com.hanlanguage.hanbook:id/recyclerMoreBook'  # 书籍列表


class AllWordPage(BasePage):
    activity = '.flash.ui.view.WordsListActivity'  #

    tvCenterTitle = 'com.hanlanguage.hanbook:id/tvCenterTitle'

    tvWordNum = 'com.hanlanguage.hanbook:id/tvWordNum'
    tvWordType = 'com.hanlanguage.hanbook:id/tvWordType'
    slideRecyclerWords = 'com.hanlanguage.hanbook:id/slideRecyclerWords'  # 词列表

    notLearned = '//*[@resource-id="com.hanlanguage.hanbook:id/recycler"]/android.widget.RelativeLayout[0]'
    learned = '//*[@resource-id="com.hanlanguage.hanbook:id/recycler"]/android.widget.RelativeLayout[1]'


class BookDetailPage(BasePage):
    activity = '.flash.ui.view.BookDetailActivity'

    tvCenterTitle = 'com.hanlanguage.hanbook:id/tvCenterTitle'
    tvTitleRight = 'com.hanlanguage.hanbook:id/tvTitleRight'
    imageClose = 'com.hanlanguage.hanbook:id/imageClose'

    add = 'com.hanlanguage.hanbook:id/tvAdd'
    done = 'com.hanlanguage.hanbook:id/tvDone'


class WordBookGuidePage(BasePage):
    activity = '.study.ui.view.wordbook.WordBookGuideActivity'

    title = 'com.hanlanguage.hanbook:id/tvCenterTitle'

    go_study = 'com.hanlanguage.hanbook:id/tvGoStudy'
    study = 'com.hanlanguage.hanbook:id/tvStudy'
    continue_button = 'com.hanlanguage.hanbook:id/tvContinueLearn'
    study_again = 'com.hanlanguage.hanbook:id/tvStudyAgain'


class WordbookCardPage(BasePage):
    activity = '.study.ui.view.wordbook.WordBookCardsActivity'

    pause = 'com.hanlanguage.hanbook: id / imgPause'
    pause_continue = 'com.hanlanguage.hanbook: id / tvContinue'
    pause_exit = 'com.hanlanguage.hanbook: id / tvExit'

    collection = 'com.hanlanguage.hanbook:id/imgCollect'

    pinyin = 'com.hanlanguage.hanbook:id/tvPinyin'
    word = 'com.hanlanguage.hanbook:id/tvWord'
    audio = 'com.hanlanguage.hanbook:id/lavWordAudio'
    explain = 'com.hanlanguage.hanbook:id/ctlExplain'
    read = 'com.hanlanguage.hanbook:id/llBottomRead'
    write = 'com.hanlanguage.hanbook:id/llBottomWrite'
    detail = 'com.hanlanguage.hanbook:id/llBottomDetail'

    detail = 'com.hanlanguage.hanbook:id/tvSpeed'
    audio = 'com.hanlanguage.hanbook:id/ctlOperateAudio'
    hide = 'com.hanlanguage.hanbook:id/ctlRightLayout'
    hide_pinyin = 'com.hanlanguage.hanbook:id/tvHidePinyin'
    hide_explain = 'com.hanlanguage.hanbook:id/tvHideExplain'
