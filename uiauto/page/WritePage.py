from uiauto.page.BasePage import BasePage

PACKAGE_NAME = 'com.hanlanguage.hanbook'


class WritePage(BasePage):
    activity = ".write.ui.view.WriteActivity"

    last_score = 'com.hanlanguage.hanbook:id/tvLastScore'

    previous = 'com.hanlanguage.hanbook:id/ivPrevious'
    play = 'com.hanlanguage.hanbook:id/tvPlay'
    write = 'com.hanlanguage.hanbook:id/tvWrite'
    next = 'com.hanlanguage.hanbook:id/ivNext'
    rank = 'com.hanlanguage.hanbook:id/ivRankFlag'

    write_demo = 'com.hanlanguage.hanbook:id/ivDemo'
    write_see = 'com.hanlanguage.hanbook:id/ivHint'
    write_clear = 'com.hanlanguage.hanbook:id/ivClear'
    write_back = 'com.hanlanguage.hanbook:id/ivBackspace'


class WriteResultPage(BasePage):
    activity = '.write.ui.view.WriteResultActivity'

    share = 'com.hanlanguage.hanbook:id/ivShareHover'

    share_button = 'com.hanlanguage.hanbook:id/tvShare'
    done = 'com.hanlanguage.hanbook:id/tvDone'
