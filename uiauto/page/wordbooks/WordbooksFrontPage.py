from page.BasePage import BasePage


class WordbooksFrontPage(BasePage):
    tab_name = 'com.hanlanguage.hanbook:id/tvSpeakingCards'#tab名
    topicsTitle = 'com.hanlanguage.hanbook:id/tvTopicsTitle'#标题
    tvChangeTopic = 'com.hanlanguage.hanbook:id/tvChangeTopic'#筛选按钮
    recyclerTopics = 'com.hanlanguage.hanbook:id/recyclerTopics' #speakingcard列表
    recyclerCategory = 'com.hanlanguage.hanbook:id/recyclerCategory'#筛选列表
