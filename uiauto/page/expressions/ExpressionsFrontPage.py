from uiauto.page.BasePage import BasePage


class WordbooksFrontPage(BasePage):
    recommend = 'Make your flashcards from wordbooks'  # 推荐语
    tab_name = 'com.hanlanguage.hanbook:id/tvWordBooks'  # tab名

    Ongoing = 'com.hanlanguage.hanbook:id/tvStudyTitle'
    all_words = 'com.hanlanguage.hanbook:id/tvAllWords'
    book_name = 'com.hanlanguage.hanbook:id/tvBookTitle'
    tvProcess = 'com.hanlanguage.hanbook:id/tvProcess'  # 进度百分比
    tvNotLearnNum = 'com.hanlanguage.hanbook:id/tvNotLearnNum'
    tvReviewNum = 'com.hanlanguage.hanbook:id/tvReviewNum'
    tvStudy = 'com.hanlanguage.hanbook:id/tvStudy'
    tvStudyAgain = 'com.hanlanguage.hanbook:id/tvStudyAgain'
    tvReview = 'com.hanlanguage.hanbook:id/tvReview'

    tvTitle = 'com.hanlanguage.hanbook:id/tvTitle'  # 推荐名称
    revRecommend = 'com.hanlanguage.hanbook:id/revRecommend'  # 推荐列表

    MyWordbooks = 'MyWordbooks'
    tvEdit = 'com.hanlanguage.hanbook:id/tvEdit'
    ctlAdd = 'com.hanlanguage.hanbook:id/ctlAdd'
    revWordBooks = 'com.hanlanguage.hanbook:id/revWordBooks'  # 书籍列表
