import json
import os
import sys
import time
from datetime import datetime

import requests
import xlrd
from xlutils.filter import process, XLRDReader, XLWTWriter
import han.report.report_config as config

from bs4 import BeautifulSoup

sys.path.append("..")

template = {
    0: "fail_test_report",
    1: "first_round_test_report",
    2: "online_report"
}


def getsession():
    url = "http://baichuan.hanlinguo.com/index.php?act=login"
    payload = 'username=%E5%91%A8%E4%BA%91%E8%85%BE&password=Hanbook123456'
    headers = {
        'Proxy-Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://baichuan.hanlinguo.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://baichuan.hanlinguo.com/index.php?act=login',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    session = requests.Session()
    session.request("POST", url, headers=headers, data=payload, allow_redirects=False)
    return session


session = getsession()
session.headers.update({"Cookie": config.cookie})


class Report:
    def __init__(self, report_type):
        self.report_type = report_type
        self.work_book = xlrd.open_workbook(
            config.online_report_template_url + template.__getitem__(report_type) + ".xls",
            formatting_info=True)
        # 模板表
        self.sheet_ = self.work_book.sheet_by_index(0)
        # 复制的表
        w = XLWTWriter()
        process(XLRDReader(self.work_book, 'unknown.xls'), w)
        self.style_list = w.style_list
        self.wb = w.output[0][1]
        self.sheet = self.wb.get_sheet(0)

    def write(self, row, cell, content):
        """
        更改对应表格的值
        """
        self.sheet.write(row, cell, content, self.style_list[self.sheet_.cell_xf_index(row, cell)])


def getbuglist(state=None, vid=None, level=None, page_size=500, tid=None) -> list:
    """
    state:解决状态,
    vid:版本id,
    level:bug等级,
    tid:平台（ios,android,后端,前端等）
    """
    data = {
        'pid': 51,
        'state': state,
        'vid': vid,
        'level': level,
        'pageSize': page_size,
        'tid': tid
    }

    # 自动获取的cookie 权限不够，先用手动抓取的cookie
    result = session.post(config.bug_list_url, data=data)
    res = json.loads(result.text)
    return res.get('data')


def demand():
    url = config.demand_url
    content = ''

    payload = {}
    headers = {
        'Authorization': 'Basic emhvdXl1bnRlbmc6Z1VPR0JrNkV3SjdXSnlY',
        'Cookie': 'JSESSIONID=1A645FF60B26978C2ECE0AEF5E1163EC'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(str(response.text), 'lxml')
    table_soup = BeautifulSoup(str(soup.find_all('table', class_='confluenceTable')), 'lxml')
    tr_tag = table_soup.find_all('tr')

    # content.join(tr.find('td', colspan="1").nextSibling.text for tr in tr_tag)
    for tr in tr_tag:
        td = tr.find('td', colspan="1")
        if td:
            content = content + td.nextSibling.text + "\n"

    return content


class BugData:
    def __init__(self, primeval_type, version):
        if primeval_type == 'ios':
            legacy_bug = getbuglist(tid='1,3', state='2, 1, 8')
            version_bug_list = getbuglist(vid=version, tid='1,3', state='state: 2,1,5,8,9')
        else:
            legacy_bug = getbuglist(tid='2,3', state='2, 1, 8')
            version_bug_list = getbuglist(vid=version, tid='2,3', state='state: 2,1,5,8,9')

        self.version_bug_list_number = len(version_bug_list)
        self.legacy_bug_num = len(legacy_bug)
        legacy_serious_bug = list(
            filter(lambda x: True if x.__getitem__('level') in (3, 4, 5)
                                     and x.__getitem__('cid') in (20, 13, 17) else False,
                   legacy_bug))

        self.legacy_serious_bug_titles = '\n'.join((i.__getitem__('title') for i in legacy_serious_bug))
        self.legacy_serious_bug_num = len(legacy_serious_bug)
        self.high = len(
            list(filter(lambda x: True if x.__getitem__('level') in (3, 4) else False, version_bug_list)))
        self.middle = len(list(filter(lambda x: True if x.__getitem__('level') == 2 else False, version_bug_list)))
        self.low = len(list(filter(lambda x: True if x.__getitem__('level') == 1 else False, version_bug_list)))
        self.ios = len(list(filter(lambda x: True if x.__getitem__('tid') == 1 else False, version_bug_list)))
        self.android = len(list(filter(lambda x: True if x.__getitem__('tid') == 2 else False, version_bug_list)))
        self.php = len(list(filter(lambda x: True if x.__getitem__('tid') == 3 else False, version_bug_list)))
        # self.h5 = len(list(filter(lambda x: True if x.__getitem__('tid') == 5 else False, version_bug_list)))


def online_report(report, primeval_type, version_id):
    bug_date = BugData(primeval_type, version_id)

    report.write(0, 0, config.primeval_type + ' ' + config.version + '上线报告')  # title

    report.write(4, 3, datetime.now().strftime('%Y/%m/%d'))  # 提审时间为当天

    # report.write(5, 1, demand())#  生成主要功能

    report.write(6, 1, bug_date.version_bug_list_number)
    report.write(6, 3, bug_date.legacy_bug_num)
    report.write(6, 5, bug_date.legacy_serious_bug_num)
    report.write(7, 1, bug_date.high)
    report.write(7, 3, bug_date.middle)
    report.write(7, 5, bug_date.low)

    if primeval_type == "ios":
        report.write(8, 1, bug_date.ios)
        report.write(8, 0, 'ios')
    else:
        report.write(8, 1, bug_date.android)
        report.write(8, 0, 'android')
    report.write(8, 3, bug_date.php)
    report.write(9, 1, bug_date.legacy_serious_bug_titles)


def fail_test_report(report, primeval_type, version_id):
    if primeval_type == 'ios':
        bug = getbuglist(tid='1,3,5', vid=version_id)
    else:
        bug = getbuglist(tid='2,3,5', vid=version_id)

    bug_list = (i.__getitem__("title") for i in bug)
    report.write(5, 1, '\n'.join(bug_list))


def first_round_test_report(report, primeval_type, version_id):
    bug_date = BugData(primeval_type, version_id)
    report.write(6, 1, bug_date.version_bug_list_number)
    report.write(6, 3, bug_date.legacy_bug_num)
    report.write(7, 1, bug_date.high)
    report.write(7, 3, bug_date.middle)
    report.write(7, 5, bug_date.low)

    if primeval_type == "ios":
        report.write(8, 1, bug_date.ios)
        report.write(8, 0, 'ios')
    else:
        report.write(8, 1, bug_date.android)
        report.write(8, 0, 'android')
    report.write(8, 3, bug_date.php)

    pass


def generate_report(report_type, primeval_type, version):
    report = Report(report_type)

    def get_map(url, payload=None, has_data=0) -> list:
        headers = {
            'Proxy-Connection': 'keep-alive',
            'Accept': 'text/plain, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://baichuan.hanlinguo.com',
            'Referer': 'http://baichuan.hanlinguo.com/admin.php?gcms=dev_bug&gmod=add&id=0&_winid=w9661&_t=688855',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        response = session.request("POST", url, headers=headers, data=payload)
        if has_data:
            res = json.loads(response.text).get('data')
        else:
            res = json.loads(response.text)
        dic = {}
        for i in res:
            dic.__setitem__(i.get("name"), i.get("id"))
        return dic

    version_id = get_map("http://baichuan.hanlinguo.com/admin.php?gcms=GX_DevType&gmod=version&pid=51&_=1632908234117")[
        version]

    """
    根据模板生成一个新的Excel报告
    """
    eval(template.__getitem__(report_type))(report, primeval_type, version_id)

    path = os.path.join(
        '%s_%s@%s.xls' % (primeval_type, template.__getitem__(report_type), time.strftime('%Y.%m.%d@%H%M%S')))
    report.wb.save(path)


if __name__ == '__main__':
    # try:
    #     opts, args = getopt.getopt(sys.argv[1:], 'r:p:v:')
    # except getopt.GetoptError:
    #     print("参数错误")
    #     sys.exit()
    #
    # if len(opts) > 0:
    #     for opt, arg in opts:
    #         print(opt, arg)
    #         if opt == "-r":
    #             report_type = arg
    #         elif opt == "-p":
    #             primeval_type = arg
    #         elif opt == "-v":
    #             version_id = arg
    #         else:
    #             print("参数错误1")
    #             sys.exit()
    #
    #     generate_report(int(report_type), primeval_type, int(version_id))
    # else:
    generate_report(config.report_type, config.primeval_type, config.version)
