import time
from multiprocessing import Process

import jsonpath
import requests
import urllib3
import xlwt
import tkinter

urllib3.disable_warnings()


def getsession():
    # target_url = 'https://miaomiao.scmttec.com/base/region/childRegions.do?'
    headers = {
        'Cookie': cookie,
        'Host': 'miaomiao.scmttec.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030522)',
        'tk': tk,
        'Referer': 'https://wx.scmttec.com/index.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'content-type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': "XMLHttpRequest"
    }
    _session = requests.Session()
    _session.headers = headers
    return _session


def new_sheet():
    _wb = xlwt.Workbook()
    _wb.add_sheet("sheet1")
    _sheet = _wb.get_sheet(0)
    return wb, _sheet


def work_runner():
    demo_url = f'https://miaomiao.scmttec.com/base/region/childRegions.do?parentCode='
    res = return_unified(
        session.request(method="GET", url=demo_url, verify=False))  # 获取全国各省的codeId
    for i in res.get('data'):  # 通过循环获取省下面的各个市的codeId
        col = 1
        num = i.get('value')  # 省codeId
        if int(num) in [11, 12, 31, 50]:  # 11, 12, 31, 50是四个直辖市的Id：北京、天津、上海、重庆。如果num在这四个值中，则不会获取下面的市Id
            time.sleep(1)
            _url = f'https://miaomiao.scmttec.com/seckill/seckill/list.do?offset=0&limit=10&regionCode={num}01'  # 获取每个市下面已有的社区信息
            result = return_unified(session.request("GET", _url, verify=False))
            list = result.get('data')
            for it in list:
                if it.get('stock') == 1:  # stock=1：代表社区可预约，还没开始
                    write_data(col, 0, i.get('name'))
                    write_data(col, 1, i.get('name'))
                    write_data(col, 2, it.get('name'))
                    write_data(col, 3, it.get('startTime'))
                    print(i.get('name') + '\t' + it.get('name') + '\t' + '开始时间：' + it.get('startTime'))
                    col = col + 1
        else:  # 如果num不在，则获取省下面的各个市的codeId
            url_par = f'https://miaomiao.scmttec.com/base/region/childRegions.do?parentCode={num}'
            res = return_unified(session.request("GET", url_par, verify=False))
            values = jsonpath.jsonpath(res, "$.data")[0]
            for value in values:
                time.sleep(1)
                s = value.get("value")
                print(str(num) + ':' + str(s))
                _url = f'https://miaomiao.scmttec.com/seckill/seckill/list.do?offset=0&limit=10&regionCode={s}'
                result = return_unified(session.request("GET", _url, verify=False))
                list = result.get('data')
                for it in list:
                    if it.get('stock') == 1:
                        write_data(col, 0, i.get('name'))
                        write_data(col, 1, value.get('name'))
                        write_data(col, 2, it.get('name'))
                        write_data(col, 3, it.get('startTime'))
                        col = col + 1
                        print(i.get('name') + '\t' + value.get('name') + '\t' + it.get(
                            'name') + '\t' + '开始时间：' + it.get('startTime'))


def write_data(row, col, mes):
    sheet.write(row, col, mes)  # ----- 按(row, col, str)写入需要写的内容 -------
    wb.save(r'D:\project\python\han\xx.xls')


def return_unified(arg, removekey=None):
    # 接口测试统一返回函数
    if arg.status_code == 200:
        try:
            return_dict = arg.json()
            return_dict["test_code"] = "success"
            return_dict["fail_message"] = ""
            if removekey:
                try:
                    del return_dict[removekey]
                except:
                    pass
        except:
            fail_data = {"test_code": "fail", "fail_message": "解析失败"}
            return fail_data
        return return_dict
    else:
        print(arg)
        return {"test_code": "fail", "fail_message": "接口调用失败"}


def reserve(**kwargs):
    # todo
    res = session.request("GET", kwargs['url'], data=kwargs['data'], verify=False)
    print(res.text.encode().decode('unicode_escape'))


def muti_process():
    for i in range(1, 11):  # 模拟并发10个客户端抢票
        kwargs = {
            'url': 'https://mapi.hanbook.com/misc/share/read?id=102385&sen=1',
            'data': '',
            'process_id': i
        }
        p = Process(target=reserve, args=(), kwargs=kwargs)
        p.start()


cookie = 'tgw_l7_route=c32cbfae4114f85df8afeb76a33d3c8f; _xxhm_=%7B%22id%22%3A19228523%2C%22mobile%22%3A%2215902379217%22%2C%22nickName%22%3A%22%E5%B0%8F%E5%91%A8%E5%B0%8F%E5%91%A8%22%2C%22headerImg%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2FdH8QVxmk2IW5FOKldRLuVpL7gwicAVnoMpice0q2zpWIqaq2dALK1xbLJ6dv1uiazuqibbMRlg30JBwQHEpJib5K2PWBTY4l9d0Kw%2F132%22%2C%22regionCode%22%3A%22500112%22%2C%22name%22%3A%22%E5%B7%A6**%22%2C%22uFrom%22%3A%22depa_vacc_detail%22%2C%22wxSubscribed%22%3A1%2C%22birthday%22%3A%221999-05-23+02%3A00%3A00%22%2C%22sex%22%3A2%2C%22hasPassword%22%3Afalse%2C%22birthdayStr%22%3A%221999-05-23%22%7D; _xzkj_=wxapptoken:10:d0a8ecfa8fba69c215a19700e297781a_f3891cc107056e6cf1c7e11cf4ad0bdc'
tk = 'wxapptoken:10:d0a8ecfa8fba69c215a19700e297781a_f3891cc107056e6cf1c7e11cf4ad0bdc'

session = getsession()
wb, sheet = new_sheet()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("500x300")
    root.title("抢")
    button = tkinter.Button(text="开始抢", command=muti_process)
    button2 = tkinter.Button(text="获取可预约列表", command=work_runner)
    button.pack()
    button2.pack()
    root.mainloop()
