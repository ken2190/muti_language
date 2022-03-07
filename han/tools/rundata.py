import json
import time

import pymysql
import requests

MYSQL_CONFIG = {
    "host": "handev-w.mysql.rds.aliyuncs.com",
    "user": "hanbook",
    "password": "IOaBLTXo9FN54VwyP3wJ",
    "database": "han_hanbook",
    "port": 3306,
    "charset": "utf8"
}

headers = {
    "Cookie": "FDX_sid=w100081_e1c13406fa4b96d2048c47f9; FDX_auth=343c1e874HFTiRN1y%2BuIm8WJeXtccYTIZMDjdXzj6pNzZaLssUQcLDtUk7RX3N9oZV9bakuV7YtJC2w6utZI%3D",
    "Host": "mapi.hancourse.net",
    "uid": "100081",
    "HB-UUID": "feb573ed2ac72c7a19622132b220ac5c",
    "HB-CLIENT-TYPE": "iOS",
    "HB-SYSVER": "12.4",
    "Accept-Language": "zh-Hans-SG;q=1, en-SG;q=0.9",
    "Accept-Encoding": "br, gzip, deflate",
    "HB-APPVER": "1.0",
    "User-Agent": "HanBook AipBot/1.0 (HanBook-IOS/1.0;  iOS/12.40; iPhone11,2",
    "HB-APPTYPE": "11",
    "HB-LANG": "zh-Hans",
    "HB-UKEY": "cccaba878687d8da5ac6fd8101edac37",
    "HB-SYSDEV": "iPhone11,2"

}


def _rundata():
    try:
        ids = []
        conn = pymysql.connect(**MYSQL_CONFIG)  # 数据库连接
        cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象

        sql_total = "SELECT count(1) as total from dc_word;"
        cur.execute(sql_total)
        total = cur.fetchone().get("total")
        step = 1000
        for i in (total // 1000):
            sql = "SELECT id from dc_word limit {},{}".format(i * 1000, 1000)
            cur.execute(sql)
            ids = cur.fetchall()
            for item in ids:
                id = (item.get("id"))
                data = {
                    "lang": 1,
                    "wid": id
                }
                url = "http://mapi.hancourse.net/dict/word/detail"
                res = requests.post(url=url, data=data, headers=headers)
                if json.loads(res.text).get('state') != 1:
                    print(id)
    finally:
        cur.close()
        conn.close()


def _rundata2():
    try:
        conn = pymysql.connect(**MYSQL_CONFIG)  # 数据库连接
        cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象

        sql_total = "SELECT id FROM dc_word WHERE state=1 and id >1001736 LIMIT 998;"

        cur.execute(sql_total)
        total = cur.fetchall()
        for result in total:
            sql = "INSERT INTO `han_hanbook`.`le_user_book_word`( `uid`, `ubid`, `aid`, `bid`, `chapter_id`, `type`, `content_id`, `wid`, `sid`, `audio`, `wscore`, `ascore`, `watched`, `explain_id`, `explain_correct`, `weight`, `state`, `ctime`, `utime`) VALUES (100469, 101904, 0, 1, 0, 0, 0, {}, 0, '', 0, 0, 0, 0, 0, 0, 0, '2022-01-04 15:16:53', '2022-01-04 15:16:53');".format(
                result['id'])
            cur.execute(sql)
            conn.commit()
    finally:
        cur.close()
        conn.close()


def _new_daily(type=None, days=0, begin_id=0):
    try:
        conn = pymysql.connect(**MYSQL_CONFIG)  # 数据库连接
        cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象
        skip = 0
        import datetime
        date = datetime.datetime(year=2022, month=2, day=1)

        while skip < days * 6:
            level = 1
            if type == 4:
                sql_total = (
                    'SELECT id, name as title ,pinyin as intro  FROM dc_word  WHERE state=1 and id>{} LIMIT {},6').format(
                    begin_id, skip)
            else:
                sql_total = (
                    'SELECT s.id id,s.zh as title,e.trans as intro FROM han_hanbook.dc_sentence  s,han_hanbook.dc_sentence_multi e WHERE s.id=e.sentence_id and s.id >3000 LIMIT {},6').format(
                    skip)
            cur.execute(sql_total)
            total = cur.fetchall()

            for i in range(6):
                id = total[i]['id']
                title = str(total[i]['title']).replace('"', '\\\"')
                intro = str(total[i]['intro']).replace('"', '\\\"')
                if type == 1 or type == 2:
                    sql = (
                        "INSERT INTO `han_hanhome`.`uc_tool_discover_sentence`(`sid`, `title`, `intro`, `level`, `number`, `hits`, `type`, `onpic`, `video`, `stime`, `etime`, `state`, `utime`, `ctime`) VALUES ({}, \"{}\", \"{}\", {}, 0, 0, {}, '', '', 0, 0, 1, '2021-12-09 16:02:13', '{}');").format(
                        id, title, intro, level, type, date)
                    print('sql__:' + sql)
                    cur.execute(sql)
                elif type == 4:
                    sql = (
                        "INSERT INTO `han_hanhome`.`uc_tool_discover_sentence`(`sid`, `title`, `intro`, `level`, `number`, `hits`, `type`, `onpic`, `video`, `stime`, `etime`, `state`, `utime`, `ctime`) VALUES ({}, \"{}\", \"{}\", {}, 0, 0, 4, '', '', 0, 0, 1, '2021-12-09 16:02:13', '{}');").format(
                        id, title, intro, level, date)
                    print('sql__:' + sql)
                    cur.execute(sql)
                    pass
                level += 1
                conn.commit()
            date = date + datetime.timedelta(days=1)
            skip += 6
    finally:
        cur.close()
        conn.close()


def _new_live_class(date="1970-01-01", type=1, classify=1, steps=4, nums=30):
    try:
        conn = pymysql.connect(**MYSQL_CONFIG)  # 数据库连接
        cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象
        from datetime import datetime

        date = date + " 00:00:00"
        begin = int(datetime.strptime(date, '%Y-%m-%d %H:%M:%S').timestamp())
        for i in range(nums):
            title = "标题—— " + "开始：" + str(begin)
            desc = "描述—— " + "开始：" + str(begin)
            sql = (
                "INSERT INTO `han_hanbook`.`li_live_preview`(`title`, `intro`, `onpic`, `tonpic`, `tname`, `link`, `stime`, `etime`, `type`, `classify`, `state`, `utime`, `ctime`) VALUES ('{}', '{}', 'image/2022/01/06/114039_61d664b7b64ea.png', '', '宝哥', 'https://mapi.hancourse.net/live/huan_tuo/watch?reconnect=2&keep_screen=1&room_id=350260848', '{}', '{}', {}, {}, 1, '2022-01-12 10:25:29', '2022-01-06 11:40:53');"). \
                format(title, desc, begin, begin + steps * 3600, type, classify)
            print('sql__:' + sql)
            cur.execute(sql)
            conn.commit()
            begin = begin + steps * 3600
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    # _new_daily(4, 30, 1001128)

    _new_live_class(date='2022-02-28', classify=2, steps=3)
