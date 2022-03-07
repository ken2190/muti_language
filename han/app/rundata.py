import requests

headers = {
    "Cookie": "FDX_sid=w100081_e1c13406fa4b96d2048c47f9; FDX_auth=343c1e874HFTiRN1y%2BuIm8WJeXtccYTIZMDjdXzj6pNzZaLssUQcLDtUk7RX3N9oZV9bakuV7YtJC2w6utZI%3D"
}

if __name__ == '__main__':
    # conn = pymysql.connect(**MYSQL_CONFIG)  # 数据库连接
    # cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标对象
    #
    # sql_total = "SELECT count(1) from dc_word;"
    # cur.execute(sql_total)
    # total = cur.fetchone()
    # step = 1000
    # for i in int(total / 1000):
    #     sql = "SELECT id from dc_word limit {},{}".format(i * 1000, 1000)
    #     cur.execute(sql)
    #     items = cur.fetchall()
    #     for item in items:
    #         id = (item.get("id"))
    #         res = requests.post(url="https://mapi.hancourse.net/dict/word/detail", data="lang=1&wid={}".format(id),
    #                             headers=headers)
    #         print(res)
    #
    #     cur.close()
    #     conn.close()
    data = "lang=1&wid={}".format(id)
    url = "https://mapi.hancourse.net/dict/word/detail"
    res = requests.post(url=url, data=data, headers=headers)

    print(res)
