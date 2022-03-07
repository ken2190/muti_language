from uiauto.page.BasePage import BasePage


class BookDetailPage(BasePage):
    activity = '.flash.ui.view.BookDetailActivity'

    tvCenterTitle = 'com.hanlanguage.hanbook:id/tvCenterTitle'
    tvTitleRight = 'com.hanlanguage.hanbook:id/tvTitleRight'
    imageClose = 'com.hanlanguage.hanbook:id/imageClose'

    tvAdd = 'com.hanlanguage.hanbook:id/tvAdd'
    tvDone = 'com.hanlanguage.hanbook:id/tvDone'
