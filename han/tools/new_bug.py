import json
import os
import time
import requests
import tkinter as tk
from tkinter import ttk

global cookie
cookie = "cmsSid=f89822f2aaaa05a05cecd434626a44e3; cms_Logid=3997"
content = '''
【步骤】
1、
2、
【问题】


 
【期望】


【备注】


'''

screen = {
    "无": 0,
    "android": 1,
    "ios": 2
}


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
        'Cookie': cookie
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if has_data:
        res = json.loads(response.text).get('data')
    else:
        res = json.loads(response.text)
    dic = {}
    for i in res:
        dic.__setitem__(i.get("name"), i.get("id"))
    return dic


def go():
    users = get_map("http://baichuan.hanlinguo.com/admin.php?gcms=GX_DevType&gmod=userlist&pid=51",
                    "pageIndex=0&pageSize=100&sortField=&sortOrder=", has_data=1)

    version = get_map("http://baichuan.hanlinguo.com/admin.php?gcms=GX_DevType&gmod=version&pid=51&_=1632908234117")

    level = get_map("http://baichuan.hanlinguo.com/admin.php?gcms=GX_DevType&gmod=Level&_=1632908234114")

    type = get_map("http://baichuan.hanlinguo.com/admin.php?gcms=GX_DevType&gmod=bugclass&_=1632908234115")

    platform = get_map("http://baichuan.hanlinguo.com/admin.php?gcms=GX_DevType&gmod=bugType&_=1632908234116")

    root = tk.Tk()
    root.title('提交bug')
    width = 570
    height = 500
    xscreen = root.winfo_screenwidth()
    yscreen = root.winfo_screenheight()
    xmiddle = (xscreen - width) / 2
    ymiddle = (yscreen - height) / 2
    root.geometry('%dx%d+%d+%d' % (width, height, xmiddle, ymiddle))

    titlel = tk.Label(root, text="标题：")
    titlel.grid(column=0, row=1)
    title = tk.Text(root, width=55, height=5, bg='#f0f0f0')
    title.grid(column=1, row=1)

    textl = tk.Label(root, text="内容：")
    textl.grid(column=0, row=2)
    text = tk.Text(root, width=55, height=15, bg='#f0f0f0')
    text.grid(column=1, row=2)
    text.insert('end', content)

    # 创建一个下拉列表
    w = tk.Label(root, text="版本：")
    w.grid(column=0, row=3)
    versionlist = tk.StringVar()
    versionChosen = ttk.Combobox(root, width=12, textvariable=versionlist)
    versionChosen['values'] = tuple([i for i in version.keys()])
    versionChosen.grid(column=1, row=3)  # 设置其在界面中出现的位置  column代表列   row 代表行
    versionChosen.current(0)
    # 创建一个下拉列表
    levell = tk.Label(root, text="错误等级：")
    levell.grid(column=0, row=4)
    levellist = tk.StringVar()
    levelChosen = ttk.Combobox(root, width=12, textvariable=levellist)
    levelChosen['values'] = tuple([i for i in level.keys()])
    levelChosen.grid(column=1, row=4)  # 设置其在界面中出现的位置  column代表列   row 代表行
    levelChosen.current(2)

    # 创建一个下拉列表
    typel = tk.Label(root, text="类型：")
    typel.grid(column=0, row=5)
    typelist = tk.StringVar()
    typeChosen = ttk.Combobox(root, width=12, textvariable=typelist)
    typeChosen['values'] = tuple([i for i in type.keys()])
    typeChosen.grid(column=1, row=5)  # 设置其在界面中出现的位置  column代表列   row 代表行
    typeChosen.current(1)

    # 创建一个下拉列表
    platforml = tk.Label(root, text="平台：")
    platforml.grid(column=0, row=6)
    platformlist = tk.StringVar()
    platformChosen = ttk.Combobox(root, width=12, textvariable=platformlist)
    platformChosen['values'] = tuple([i for i in platform.keys()])
    platformChosen.grid(column=1, row=6)  # 设置其在界面中出现的位置  column代表列   row 代表行
    platformChosen.current(0)

    # 创建一个下拉列表
    screenl = tk.Label(root, text="截图：")
    screenl.grid(column=0, row=7)
    screenlist = tk.StringVar()
    screenChosen = ttk.Combobox(root, width=12, textvariable=screenlist)
    screenChosen['values'] = tuple([i for i in screen.keys()])
    screenChosen.grid(column=1, row=7)  # 设置其在界面中出现的位置  column代表列   row 代表行
    screenChosen.current(0)

    # 创建一个下拉列表
    usersl = tk.Label(root, text="指派给：")
    usersl.grid(column=0, row=8)
    userlist = tk.StringVar()
    userChosen = ttk.Combobox(root, width=12, textvariable=userlist)
    userChosen['values'] = tuple(users.keys())
    userChosen.grid(column=1, row=8)  # 设置其在界面中出现的位置  column代表列   row 代表行
    userChosen.current(0)

    def getvalues():
        createbug(title=title.get("0.0", "end"),
                  content=text.get("0.0", "end"),
                  tid=platform[platformlist.get()],
                  uid=users[userlist.get()],
                  uname=userlist.get(),
                  screen=screen[screenlist.get()],
                  vid=version[versionlist.get()],
                  level=level[levellist.get()],
                  cid=type[typelist.get()]
                  )

    but2 = tk.Button(root, text="提bug", command=getvalues, bg='#dfdfdf')
    but2.grid(row=9, columnspan=5, pady='10')
    root.mainloop()


def screenshot(screen):
    if screen == 0:
        return None
    name = int(time.time())
    path = "D:\project\python\muti_language\han\\png/{}.png".format(name)
    if screen == 1:
        android_path = "/sdcard/{}.png".format(name)
        os.system("adb shell screencap  -p /sdcard/{}.png".format(name))
        os.system("adb pull " + android_path + " " + path)
    elif screen == 2:
        os.system("tidevice screenshot " + path)
    img = open(path, 'rb')
    file = {
        'fileData': (path.format(name), img, 'Content-Type: image/jpg')}
    return file


def createbug(title, tid, uid, uname, screen=0, content=None, vid=454, level=3, cid=13):
    if not content:
        content = title
    data = {
        "title": title,
        "content": content,
        "vid": vid,
        "level": level,
        "cid": cid,
        "tid": tid,
        "uid": uid,
        "uname": uname,
        "pagesize": 50,
        "pid": 51
    }

    file = screenshot(screen)
    if file:
        body = {
            "name": "screenshot.png",
            "id": 51,
            "type": "team"
        }
        res = requests.post(url="http://baichuan.hanlinguo.com/sigapi.php?mod=CMSatth", data=body, files=file,
                            headers={'Cookie': cookie})
        atthid = json.loads(res.text).get('msg').get('id')
        data["atthid"] = atthid

    result = requests.post("http://baichuan.hanlinguo.com/admin.php?gcms=dev_bug&gmod=add&_winid=w8121&_t=133010",
                           data=data, headers={'Cookie': cookie})
    print(result)


if __name__ == '__main__':
    go()
    # screenshot(1)
    # screenshot(2)
    pass
