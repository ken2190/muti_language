from uiauto.page.BasePage import BasePage


class WebViewPage(BasePage):
    activity = '.main.ui.view.WebViewActivity'

    title = 'com.hanlanguage.hanbook:id/tvCenterTitle'


class PinyinPage(BasePage):
    f = '//*[@text="f"]'

    video_close = 'com.hanlanguage.hanbook:id/imgClose'

    layer_close = 'com.hanlanguage.hanbook:id/imageClose'

    play = 'com.hanlanguage.hanbook:id/imgPlayBtn'
