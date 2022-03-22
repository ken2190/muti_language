from uiauto.page.BasePage import BasePage

PACKAGE_NAME = 'com.hanlanguage.hanbook'


class ReadPage(BasePage):
    activity = ".read.ui.view.ReadActivity"

    # todo


class ReadResultPage(BasePage):
    activity = '.read.ui.view.ReadResultActivity'

    share = 'com.hanlanguage.hanbook:id/imgShare'
    myrecord = 'com.hanlanguage.hanbook:id/tvMyRecord'

    share_button = 'com.hanlanguage.hanbook:id/tvShare'
    done = 'com.hanlanguage.hanbook:id/tvDone'
