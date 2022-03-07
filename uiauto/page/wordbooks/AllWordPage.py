from page.BasePage import BasePage


class AllWordPage(BasePage):
    activity = '.flash.ui.view.WordsListActivity'  #

    tvCenterTitle = 'com.hanlanguage.hanbook:id/tvCenterTitle'

    tvWordNum = 'com.hanlanguage.hanbook:id/tvWordNum'
    tvWordType = 'com.hanlanguage.hanbook:id/tvWordType'
    slideRecyclerWords = 'com.hanlanguage.hanbook:id/slideRecyclerWords'  # 词列表

    notLearned = '//*[@resource-id="com.hanlanguage.hanbook:id/recycler"]/android.widget.RelativeLayout[0]'
    learned = '//*[@resource-id="com.hanlanguage.hanbook:id/recycler"]/android.widget.RelativeLayout[1]'
