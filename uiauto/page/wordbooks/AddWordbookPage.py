from uiauto.page.BasePage import BasePage


class AddWordbookPage(BasePage):
    activity = '.flash.ui.view.WordsListActivity'  #

    tvCenterTitle = 'com.hanlanguage.hanbook:id/tvCenterTitle'

    ctlTextbooks = 'com.hanlanguage.hanbook:id/ctlTextbooks'
    ctlIndustries = 'com.hanlanguage.hanbook:id/ctlIndustries'
    ctlSubjects = 'com.hanlanguage.hanbook:id/ctlSubjects'
    recyclerView = 'com.hanlanguage.hanbook:id/recyclerView'  # 专集列表

    tvShelfUnfold = 'com.hanlanguage.hanbook:id/tvShelfUnfold'  # 展开收起
    recyclerMoreBook = 'com.hanlanguage.hanbook:id/recyclerMoreBook'  # 书籍列表
