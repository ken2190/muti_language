import time
import unittest

from uiautomator2 import Direction
from uiauto.page import DictionaryPage, SearchPage, WordsDetailPage, CameraPage, DailyPrevious
from uiauto.page import MainPage
from uiauto.page import WebViewPage, PinyinPage
from uiauto.page import ExpressionsPage, SpeakingCardGuidePage, ExpressionsCardPage
from uiauto.page import MePage, MeInformationPage, MyCollectionPage, HistoryPage, FeedbackListPage, SetPage, MessagePage
from uiauto.page import WriteResultPage
from uiauto.page import ReadResultPage, ReadPage
from uiauto.page import WritePage
from uiauto.page import FeedBackPage
from uiauto.page import CoursePage, ClassDetailPage, VideoPage, QuestionPage
from uiauto.page import WordbookCardPage, AllWordPage, AddWordbookPage, MyWordbookPage, WordBookGuidePage, \
    BookDetailPage

from uiauto.device.device import BaseDevice

device = BaseDevice('192.168.0.107')


class TestMe(unittest.TestCase):

    def __init__(self, device):
        super(TestMe, self).__init__()
        self.d = device

    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)

    def tearDown(self) -> None:
        device.back()

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_in_me_information(self):
        device.click_up_until_exits(MePage.top_avatar)
        self.assertTrue(device.device.wait_activity(MeInformationPage.activity))

    def test_in_setting(self):
        device.click_up_until_exits(MePage.top_setting)
        self.assertTrue(device.device.wait_activity(SetPage.activity))

    # def test_in_colloction(self):
    #     device.click_up_until_exits(MePage.collection)
    #     self.assertTrue(device.device.wait_activity(MyCollectionPage.activity))
    #
    # def test_in_history(self):
    #     device.click_up_until_exits(MePage.history)
    #     self.assertTrue(device.device.wait_activity(HistoryPage.activity))

    # def test_in_feedback(self):
    #     device.click_up_until_exits(MePage.feedback)
    #     self.assertTrue(device.device.wait_activity(FeedbackListPage.activity))

    def test_in_message(self):
        device.click_up_until_exits(MePage.message)
        self.assertTrue(device.device.wait_activity(MessagePage.activity))

    def test_in_update(self):
        device.click_down_until_exits(MePage.link_update)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))

    # def test_in_1to1(self):
    #     device.click_down_until_exits(MePage.link_1to1)
    #     self.assertTrue(device.device.wait_activity(WebViewPage.activity))
    #
    # def test_in_invite(self):
    #     device.click_down_until_exits(MePage.link_invite)
    #     self.assertTrue(device.device.wait_activity(WebViewPage.activity))

    # def test_me(self):
    #     de.swip(Direction.UP)
    #     if not de.exits(MePage.course_subscribed):
    #         de.click(MePage.course_subscribe)
    #         # todo
    #     de.click(MePage.link_facebook)
    #     self.assertTrue(de.device.wait_activity(WebViewPage.activity))
    #     de.back()
    #
    #     de.click(MePage.link_whatsapp)
    #     self.assertTrue(de.device.wait_activity(WebViewPage.activity))
    #     de.back()
    #
    #     de.click(MePage.link_playorstore)
    #     self.assertTrue(de.device.wait_activity(WebViewPage.activity))
    #     de.back()


class TestCollection(unittest.TestCase):
    print("TestCollection")

    # device = BaseDevice()

    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.collection)

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_collection(self):
        self.assertTrue(device.device.wait_activity(MyCollectionPage.activity))

        device.click(MyCollectionPage.edit)
        device.locate(MyCollectionPage.list).child()[1].click()
        device.click(MyCollectionPage.multi_delete)
        device.click(MyCollectionPage.confirm)
        device.click(MyCollectionPage.done)

        device.click(MyCollectionPage.studyInFlash)
        device.device.press("back")


class TestHistory(unittest.TestCase):
    print("TestHistory")

    # device = BaseDevice()

    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.history)

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_history(self):
        self.assertTrue(device.device.wait_activity(HistoryPage.activity))
        device.click_down_until_exits(HistoryPage.write, always=True)
        self.assertTrue(device.device.wait_activity(WriteResultPage.activity))
        device.back()
        device.click_down_until_exits(HistoryPage.read, always=True)
        self.assertTrue(device.device.wait_activity(ReadResultPage.activity))
        device.back()


class TestFeedbackList(unittest.TestCase):
    # device = BaseDevice()

    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.feedback)

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_feedback_list(self):
        self.assertTrue(device.device.wait_activity(FeedbackListPage.activity))
        device.click(FeedbackListPage.feedback)
        self.assertTrue(device.device.wait_activity(FeedBackPage.activity))
        device.back()
        device.click(FeedbackListPage.faq)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.back()


class TestFeedback(unittest.TestCase):

    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.feedback)
        self.assertTrue(device.device.wait_activity(FeedbackListPage.activity))
        device.click(FeedbackListPage.feedback)
        print("setUp成功")

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_feedback(self):
        self.assertTrue(device.device.wait_activity(FeedBackPage.activity))
        device.locate(FeedBackPage.option_list).child()[1].click()
        device.locate(FeedBackPage.text).send_keys("测试反馈")
        device.back()
        device.locate(FeedBackPage.email).send_keys("1084883809@qq.com")
        device.back()
        device.click(FeedBackPage.submit)


class TestDictionary(unittest.TestCase):
    # device = BaseDevice()

    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Dictionary)
        print("setUp成功")

    def tearDown(self) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_search(self):
        device.click(DictionaryPage.search_box)
        self.assertTrue(device.device.wait_activity(SearchPage.activity))

        device.locate(SearchPage.content).send_keys("你好")
        device.locate(SearchPage.result_list).child()[0].click()
        self.assertTrue(device.device.wait_activity(WordsDetailPage.activity))
        device.click(WordsDetailPage.collection)
        device.back()
        self.assertTrue(device.device.wait_activity(SearchPage.activity))

        device.locate(SearchPage.content).clear_text()
        device.locate(SearchPage.content).send_keys("一")
        device.locate(SearchPage.result_list).child()[0].click()
        self.assertTrue(device.device.wait_activity(WordsDetailPage.activity))
        device.click(WordsDetailPage.collection)
        device.back()

    def test_yuyin(self):
        device.click(DictionaryPage.search_speech)
        with device.device.watch_context() as ctx:
            ctx.when(SearchPage.permission).click()
        self.assertTrue(device.device.wait_activity(SearchPage.activity))

        self.assertTrue(device.exits(SearchPage.speech_record))

    def test_write(self):
        device.click(DictionaryPage.search_write)
        self.assertTrue(device.device.wait_activity(SearchPage.activity))
        self.assertTrue(device.exits(SearchPage.write_eraser))

    def test_camera(self):
        device.click(DictionaryPage.search_camera)
        time.sleep(1)
        with device.device.watch_context() as ctx:
            ctx.when(CameraPage.permission).click()
        # device.device.watcher.run()

        self.assertTrue(device.device.wait_activity(CameraPage.activity))
        device.click(CameraPage.take_photo)
        self.assertTrue(device.exits(CameraPage.choose))

    def test_pinyin_search(self):
        device.click(DictionaryPage.search_pinyin)
        self.assertTrue(device.device.wait_activity(SearchPage.activity))
        device.click('b')
        device.click('ba')
        device.click('把')
        device.click(SearchPage.done)
        self.assertTrue(device.device.wait_activity(WordsDetailPage.activity))

    def test_daily_read(self):
        device.click(DictionaryPage.daily_read)
        self.assertTrue(device.device.wait_activity(ReadPage.activity))

    def test_daily_write(self):
        device.click(DictionaryPage.daily_write)
        self.assertTrue(device.device.wait_activity(WritePage.activity))
        # todo

    def test_daily_quiz(self):
        device.click(DictionaryPage.daily_quiz)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))

    def test_daily_previous(self):
        device.click(DictionaryPage.daily_previous)
        self.assertTrue(device.device.wait_activity(DailyPrevious.activity))

    def test_radical_search(self):
        device.click(DictionaryPage.search_radicals)
        self.assertTrue(device.device.wait_activity(SearchPage.activity))
        device.click('一')
        time.sleep(0.5)
        device.click('七')
        device.click(SearchPage.done)
        self.assertTrue(device.device.wait_activity(WordsDetailPage.activity))

    def test_in_course(self):
        device.click_down_until_exits(DictionaryPage.course_ai)
        self.assertTrue(device.device.wait_activity(CoursePage.activity))
        device.click(MainPage.Dictionary)
        print("test_in_course成功")

    def test_in_live(self):
        device.click_down_until_exits(DictionaryPage.course_live)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.back()
        print("test_in_live成功")

    # def test_in_pinyin(self):
    #     device.click_down_until_exits(DictionaryPage.course_pinyin)
    #     self.assertTrue(device.device.wait_activity(WebViewPage.activity))
    #     device.back()
    #     print("test_in_pinyin成功")

    def test_pinyin_video(self):
        device.click_down_until_exits(DictionaryPage.course_pinyin)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.click_down_until_exits(PinyinPage.f)
        device.click(PinyinPage.play)
        time.sleep(10)
        device.back()
        time.sleep(1)
        device.back()  # 弹层关闭
        time.sleep(1)
        device.back()

    def test_speaking_card(self):
        device.click_down_until_exits(DictionaryPage.course_speakingcard)

        self.assertTrue(device.device.wait_activity(ExpressionsPage.activity))

        device.click(ExpressionsPage.not_finished_continue)
        self.assertTrue(device.device.wait_activity(SpeakingCardGuidePage.activity))
        device.click(SpeakingCardGuidePage.continue_button)
        self.assertTrue(device.device.wait_activity(ExpressionsCardPage.activity))

        device.click(ExpressionsCardPage.pause)
        device.click(ExpressionsCardPage.pause_exit)
        self.assertTrue(device.device.wait_activity(SpeakingCardGuidePage.activity), str(device.device.app_current))
        device.back()


class TestCourse(unittest.TestCase):
    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Course)
        print("setUp成功")

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_course_main(self):
        device.click_up_until_exits(CoursePage.top_pinyin)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.back()

        device.click_up_until_exits(CoursePage.top_stroke)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.back()

        device.click_up_until_exits(CoursePage.top_1to1)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.back()

        device.click_up_until_exits(CoursePage.top_speakingcard)
        self.assertTrue(device.device.wait_activity(ExpressionsPage.activity))
        device.back()

        device.click_up_until_exits(CoursePage.live_class)
        self.assertTrue(device.device.wait_activity(WebViewPage.activity))
        device.back()

        device.click_down_until_exits(CoursePage.ai_first_course)
        self.assertTrue(device.device.wait_activity(ClassDetailPage.activity))
        device.back()


class Test_watch_cousre(unittest.TestCase):
    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Course)
        device.click_down_until_exits(CoursePage.ai_first_course)
        self.assertTrue(device.device.wait_activity(ClassDetailPage.activity))
        device.click(ClassDetailPage.first_node)
        print("setUp成功")

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_watch(self):
        self.assertTrue(device.device.wait_activity(VideoPage.activity))
        if device.exits(VideoPage.cotinue_cancel):
            device.click(VideoPage.cotinue_cancel)

        device.swip(Direction.LEFT)
        time.sleep(30)
        device.click(VideoPage.continue_button)

        self.assertTrue(device.device.wait_activity(QuestionPage.activity))
        device.click(QuestionPage.question_close)
        if device.exits(VideoPage.video_close_no):
            device.click(VideoPage.video_close_no)


class TestWordBook(unittest.TestCase):
    def setUp(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(DictionaryPage.wordbook_my)
        self.assertTrue(device.device.wait_activity(MyWordbookPage.activity))

    def tearDown(self) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    @classmethod
    def tearDownClass(cls) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_allwords(self):
        device.click(MyWordbookPage.ongoing_allwords)
        self.assertTrue(device.device.wait_activity(AllWordPage.activity))

    def test_add_book(self):
        device.click_down_until_exits(MyWordbookPage.mywordbook_add)
        self.assertTrue(device.device.wait_activity(AddWordbookPage.activity))

        device.locate(AddWordbookPage.list).child(text='Unfold').click()
        self.assertTrue(device.exits('Fold'))
        device.locate(AddWordbookPage.book_list).child()[0].click()
        self.assertTrue(device.device.wait_activity(BookDetailPage.activity))
        device.click(BookDetailPage.add)

        self.assertTrue(device.exits(BookDetailPage.done))

    def test_delete_book(self):
        device.click(MyWordbookPage.mywordbook_edit)
        self.assertTrue(device.exits(MyWordbookPage.mywordbook_done))
        device.locate('Common tableware').sibling(resourceId=MyWordbookPage.mywordbook_delete).click()
        device.click(MyWordbookPage.mywordbook_delete_yes)
        device.click(MyWordbookPage.mywordbook_done)

    def test_study_wordbook(self):
        device.locate('NPCR Textbook 3').sibling(resourceId=MyWordbookPage.mywordbook_book_cover).click()
        self.assertTrue(device.device.wait_activity(WordBookGuidePage.activity))
        if device.exits(WordBookGuidePage.go_study):
            device.click(WordBookGuidePage.go_study)
        else:
            device.click(WordBookGuidePage.study)
        self.assertTrue(device.device.wait_activity(WordbookCardPage.activity))

        for i in range(5):
            device.swip(Direction.LEFT)
            time.sleep(1.1)
        if device.exits(WordbookCardPage.collection):
            device.click(WordbookCardPage.collection)


if __name__ == '__main__':
    unittest.main()
