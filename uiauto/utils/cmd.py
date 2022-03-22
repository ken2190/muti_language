import os


def download(url, save_path, domain='https://c2.hancourse.com'):
    if url.__contains__('http'):
        path = url
    else:
        path = domain + url
        str(url).find()

    shell = "powershell (new-object System.Net.WebClient).DownloadFile('{}','{}' )".format(path, save_path)
    try:
        os.system(shell)
        print('下载成功')
    except OSError as e:
        print('下载失败')


if __name__ == '__main__':
    url = '/app/2022/1.6.3/app-hb_fanzhifei-release_163_jiagu_sign.apk'
    # url = 'https://down.hanbook.com/down/index?v=1000'
    save_path = 'd:/app-hb_fanzhifei-release_163_jiagu_sign.apk'
    download(url, save_path)
