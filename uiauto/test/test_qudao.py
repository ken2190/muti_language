import time

import pytest
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
from uiauto.runner import devices
from uiauto.device.device import BaseDevice

device = None
address = None


def setup_module():
    global address
    address = devices.pop()
    global device
    device = BaseDevice()(address)
    device.device.app_stop_all()
    print("执行了setup_module")


def teardown_module():
    devices.append(address)


class TestMe:

    def setup(self) -> None:
        print("执行TestMesetUp")
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)

    def teardown(self) -> None:
        device.back()

    def teardown_class(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_in_me_information(self):
        print("执行了test_in_me_information")
        device.click_up_until_exits(MePage.top_avatar)
        assert device.device.wait_activity(MeInformationPage.activity)

    def test_in_setting(self):
        device.click_up_until_exits(MePage.top_setting)
        assert device.device.wait_activity(SetPage.activity)

    # def test_in_colloction(self,device):
    #     device.click_up_until_exits(MePage.collection)
    #     assert device.device.wait_activity(MyCollectionPage.activity)
    #
    # def test_in_history(self,device):
    #     device.click_up_until_exits(MePage.history)
    #     assert device.device.wait_activity(HistoryPage.activity)

    # def test_in_feedback(self,device):
    #     device.click_up_until_exits(MePage.feedback)
    #     assert device.device.wait_activity(FeedbackListPage.activity)

    def test_in_message(self):
        device.click_up_until_exits(MePage.message)
        assert device.device.wait_activity(MessagePage.activity)

    def test_in_update(self):
        device.click_down_until_exits(MePage.link_update)
        assert device.device.wait_activity(WebViewPage.activity)

    # def test_in_1to1(self,device):
    #     device.click_down_until_exits(MePage.link_1to1)
    #     assert device.device.wait_activity(WebViewPage.activity)
    #
    # def test_in_invite(self,device):
    #     device.click_down_until_exits(MePage.link_invite)
    #     assert device.device.wait_activity(WebViewPage.activity)

    # def test_me(self,device):
    #     de.swip(Direction.UP)
    #     if not de.exits(MePage.course_subscribed):
    #         de.click(MePage.course_subscribe)
    #         # todo
    #     de.click(MePage.link_facebook)
    #     assert de.device.wait_activity(WebViewPage.activity)
    #     de.back()
    #
    #     de.click(MePage.link_whatsapp)
    #     assert de.device.wait_activity(WebViewPage.activity)
    #     de.back()
    #
    #     de.click(MePage.link_playorstore)
    #     assert de.device.wait_activity(WebViewPage.activity)
    #     de.back()


class TestCollection():
    print("TestCollection")

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.collection)

    def teardown_class(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_collection(self):
        assert device.device.wait_activity(MyCollectionPage.activity)

        device.click(MyCollectionPage.edit)
        device.locate(MyCollectionPage.list).child()[1].click()
        device.click(MyCollectionPage.multi_delete)
        device.click(MyCollectionPage.confirm)
        device.click(MyCollectionPage.done)

        device.click(MyCollectionPage.studyInFlash)
        device.device.press("back")


class TestHistory():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.history)

    def teardown_class(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    @pytest.mark.flaky(rerun=1)
    def test_history(self):
        assert device.device.wait_activity(HistoryPage.activity)
        device.click_down_until_exits(HistoryPage.write, always=True)
        assert device.device.wait_activity(WriteResultPage.activity)
        device.back()
        device.click_down_until_exits(HistoryPage.read, always=True)
        assert device.device.wait_activity(ReadResultPage.activity)
        device.back()


class TestFeedbackList():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.feedback)

    def teardown(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_feedback_list(self):
        assert device.device.wait_activity(FeedbackListPage.activity)
        device.click(FeedbackListPage.feedback)
        assert device.device.wait_activity(FeedBackPage.activity)
        device.back()
        device.click(FeedbackListPage.faq)
        assert device.device.wait_activity(WebViewPage.activity)
        device.back()


class TestFeedback():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Me)
        device.click(MePage.feedback)
        assert device.device.wait_activity(FeedbackListPage.activity)
        device.click(FeedbackListPage.feedback)
        print("setUp成功")

    def teardown(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_feedback(self):
        assert device.device.wait_activity(FeedBackPage.activity)
        device.locate(FeedBackPage.option_list).child()[1].click()
        device.locate(FeedBackPage.text).send_keys("测试反馈")
        device.back()
        device.locate(FeedBackPage.email).send_keys("1084883809@qq.com")
        device.back()
        device.click(FeedBackPage.submit)


class TestDictionary():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Dictionary)
        print("setUp成功")

    def teardown(self) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_search(self):
        device.click(DictionaryPage.search_box)
        assert device.device.wait_activity(SearchPage.activity)

        device.locate(SearchPage.content).send_keys("你好")
        device.locate(SearchPage.result_list).child()[0].click()
        assert device.device.wait_activity(WordsDetailPage.activity)
        device.click(WordsDetailPage.collection)
        device.back()
        assert device.device.wait_activity(SearchPage.activity)

        device.locate(SearchPage.content).clear_text()
        device.locate(SearchPage.content).send_keys("一")
        device.locate(SearchPage.result_list).child()[0].click()
        assert device.device.wait_activity(WordsDetailPage.activity)
        device.click(WordsDetailPage.collection)
        device.back()

    def test_yuyin(self):
        device.click(DictionaryPage.search_speech)
        with device.device.watch_context() as ctx:
            ctx.when(SearchPage.permission).click()
        assert device.device.wait_activity(SearchPage.activity)

        assert device.exits(SearchPage.speech_record)

    def test_write(self):
        device.click(DictionaryPage.search_write)
        assert device.device.wait_activity(SearchPage.activity)
        assert device.exits(SearchPage.write_eraser)

    def test_camera(self):
        device.click(DictionaryPage.search_camera)
        time.sleep(1)
        with device.device.watch_context() as ctx:
            ctx.when(CameraPage.permission).click()
        # device.device.watcher.run()

        assert device.device.wait_activity(CameraPage.activity)
        device.click(CameraPage.take_photo)
        assert device.exits(CameraPage.choose)

    def test_pinyin_search(self):
        device.click(DictionaryPage.search_pinyin)
        assert device.device.wait_activity(SearchPage.activity)
        device.click('b')
        device.click('ba')
        device.click('把')
        device.click(SearchPage.done)
        assert device.device.wait_activity(WordsDetailPage.activity)

    def test_daily_read(self):
        device.click(DictionaryPage.daily_read)
        assert device.device.wait_activity(ReadPage.activity)

    def test_daily_write(self):
        device.click(DictionaryPage.daily_write)
        assert device.device.wait_activity(WritePage.activity)
        # todo

    def test_daily_quiz(self):
        device.click(DictionaryPage.daily_quiz)
        assert device.device.wait_activity(WebViewPage.activity)

    def test_daily_previous(self):
        device.click(DictionaryPage.daily_previous)
        assert device.device.wait_activity(DailyPrevious.activity)

    def test_radical_search(self):
        device.click(DictionaryPage.search_radicals)
        assert device.device.wait_activity(SearchPage.activity)
        device.click('一')
        time.sleep(0.5)
        device.click('七')
        device.click(SearchPage.done)
        assert device.device.wait_activity(WordsDetailPage.activity)

    def test_in_course(self):
        device.click_down_until_exits(DictionaryPage.course_ai)
        assert device.device.wait_activity(CoursePage.activity)
        device.click(MainPage.Dictionary)
        print("test_in_course成功")

    def test_in_live(self):
        device.click_down_until_exits(DictionaryPage.course_live)
        assert device.device.wait_activity(WebViewPage.activity)
        device.back()
        print("test_in_live成功")

    # def test_in_pinyin(self,device):
    #     device.click_down_until_exits(DictionaryPage.course_pinyin)
    #     assert device.device.wait_activity(WebViewPage.activity)
    #     device.back()
    #     print("test_in_pinyin成功")

    def test_pinyin_video(self):
        device.click_down_until_exits(DictionaryPage.course_pinyin)
        assert device.device.wait_activity(WebViewPage.activity)
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

        assert device.device.wait_activity(ExpressionsPage.activity)

        device.click(ExpressionsPage.not_finished_continue)
        assert device.device.wait_activity(SpeakingCardGuidePage.activity)
        device.click(SpeakingCardGuidePage.continue_button)
        assert device.device.wait_activity(ExpressionsCardPage.activity)

        device.click(ExpressionsCardPage.pause)
        device.click(ExpressionsCardPage.pause_exit)
        assert device.device.wait_activity(SpeakingCardGuidePage.activity), str(device.device.app_current)
        device.back()


class TestCourse():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Course)
        print("setUp成功")

    def teardown(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_course_main(self):
        device.click_up_until_exits(CoursePage.top_pinyin)
        assert device.device.wait_activity(WebViewPage.activity)
        device.back()

        device.click_up_until_exits(CoursePage.top_stroke)
        assert device.device.wait_activity(WebViewPage.activity)
        device.back()

        device.click_up_until_exits(CoursePage.top_1to1)
        assert device.device.wait_activity(WebViewPage.activity)
        device.back()

        device.click_up_until_exits(CoursePage.top_speakingcard)
        assert device.device.wait_activity(ExpressionsPage.activity)
        device.back()

        device.click_up_until_exits(CoursePage.live_class)
        assert device.device.wait_activity(WebViewPage.activity)
        device.back()

        device.click_down_until_exits(CoursePage.ai_first_course)
        assert device.device.wait_activity(ClassDetailPage.activity)
        device.back()


class Test_watch_course():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(MainPage.Course)
        device.click_down_until_exits(CoursePage.ai_first_course)
        assert device.device.wait_activity(ClassDetailPage.activity)
        device.click(ClassDetailPage.first_node)
        print("setUp成功")

    def teardown(self):
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_watch(self):
        assert device.device.wait_activity(VideoPage.activity)
        if device.exits(VideoPage.cotinue_cancel):
            device.click(VideoPage.cotinue_cancel)

        device.swip(Direction.LEFT)
        time.sleep(30)
        device.click(VideoPage.continue_button)

        assert device.device.wait_activity(QuestionPage.activity)
        device.click(QuestionPage.question_close)
        if device.exits(VideoPage.video_close_no):
            device.click(VideoPage.video_close_no)


class TestWordBook():

    def setup(self) -> None:
        device.app_start('com.hanlanguage.hanbook')
        device.device.wait_activity(MainPage.activity)
        device.click(DictionaryPage.wordbook_my)
        assert device.device.wait_activity(MyWordbookPage.activity)

    def teardown(self) -> None:
        device.device.app_stop('com.hanlanguage.hanbook')

    def test_allwords(self):
        device.click(MyWordbookPage.ongoing_allwords)
        assert device.device.wait_activity(AllWordPage.activity)

    def test_add_book(self):
        device.click_down_until_exits(MyWordbookPage.mywordbook_add)
        assert device.device.wait_activity(AddWordbookPage.activity)

        device.locate(AddWordbookPage.list).child(text='Unfold').click()
        assert device.exits('Fold')
        device.locate(AddWordbookPage.book_list).child()[0].click()
        assert device.device.wait_activity(BookDetailPage.activity)
        device.click(BookDetailPage.add)

        assert device.exits(BookDetailPage.done)

    def test_delete_book(self):
        device.click(MyWordbookPage.mywordbook_edit)
        assert device.exits(MyWordbookPage.mywordbook_done)
        device.locate('Common tableware').sibling(resourceId=MyWordbookPage.mywordbook_delete).click()
        device.click(MyWordbookPage.mywordbook_delete_yes)
        device.click(MyWordbookPage.mywordbook_done)

    def test_study_wordbook(self):
        device.locate('NPCR Textbook 3').sibling(resourceId=MyWordbookPage.mywordbook_book_cover).click()
        assert device.device.wait_activity(WordBookGuidePage.activity)
        if device.exits(WordBookGuidePage.go_study):
            device.click(WordBookGuidePage.go_study)
        else:
            device.click(WordBookGuidePage.study)
        assert device.device.wait_activity(WordbookCardPage.activity)

        for i in range(5):
            device.swip(Direction.LEFT)
            time.sleep(1.1)
        if device.exits(WordbookCardPage.collection):
            device.click(WordbookCardPage.collection)
