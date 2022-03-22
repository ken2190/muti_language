from uiauto.page.BasePage import BasePage


class FeedBackPage(BasePage):
    activity = '.vip.ui.view.FeedBackActivity'

    option_list = 'com.hanlanguage.hanbook:id/rvFuncContainer'
    option = 'com.hanlanguage.hanbook:id/tvTag'

    text = 'com.hanlanguage.hanbook:id/etDescInput'
    email = 'com.hanlanguage.hanbook:id/etContactInput'
    submit = 'com.hanlanguage.hanbook:id/mbtSubmit'
